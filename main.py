import fastapi
from fastapi import Depends, Body, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from Models import user as user_model
from Schemas.user import UserCreateSchema, UserSchema
from Services.database.goal import create_goal
from database_initializer import get_db
from Services.database import user as user_db_services
from typing import Dict
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from Services.database.story import get_story_by_id, create_story
from Services.database.user import get_user, get_all_user_stories
from Schemas.story import StoryCreateSchema
from Schemas.goal import  GoalBase
import settings
#   from redis_initializer import redis

app = fastapi.FastAPI()



@app.post('/login', response_model=Dict)  # Эндпоинт для входа пользователя
def login(
        payload: OAuth2PasswordRequestForm = Depends(),  # Зависимость для получения данных формы
        session: Session = Depends(get_db)  # Зависимость для получения сессии базы данных
):
    """
    Этот эндпоинт обрабатывает аутентификацию пользователя.
    Он принимает данные формы в качестве входных данных, которые содержат учетные данные пользователя.
    Затем он пытается получить пользователя из базы данных с использованием предоставленного адреса электронной почты.
    Если пользователь не найден, он возвращает ошибку 401.
    Если пользователь найден, он проверяет, совпадает ли предоставленный пароль с хешированным паролем в базе данных.
    Если пароли совпадают, он генерирует и возвращает токен пользователя.
    """
    try:
        user: user_model.User = user_db_services.get_user(  # Получаем пользователя по email
            session=session, user_name=payload.username
        )
    except:
        raise HTTPException(  # Если пользователь не найден, возвращаем ошибку 401
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные пользователя"
        )

    is_validated: bool = user.validate_password(payload.password)  # Проверяем пароль пользователя
    if not is_validated:
        raise HTTPException(  # Если пароль неверный, возвращаем ошибку 401
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учетные данные пользователя"
        )
    return user.generate_token()  # Если все в порядке, возвращаем токен пользователя


@app.post("/signup", response_model=UserSchema)  # Эндпоинт для регистрации пользователя
def signup(
        payload: UserCreateSchema = Body(),  # Зависимость для получения данных формы
        session: Session = Depends(get_db)  # Зависимость для получения сессии базы данных
):
    """
    Этот эндпоинт обрабатывает регистрацию нового пользователя.
    Он принимает данные формы в качестве входных данных, которые содержат информацию для регистрации пользователя.
    Затем он хеширует пароль пользователя и создает новую запись пользователя в базе данных.
    После успешного создания пользователя он возвращает данные пользователя.
    """
    payload.hashed_password = user_model.User.hash_password(payload.hashed_password)  # Хешируем пароль пользователя
    return user_db_services.create_user(session, user=payload)  # Создаем пользователя и возвращаем его данные


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")  # Схема аутентификации OAuth2


@app.get("/profile/{username}", response_model=UserSchema)  # Эндпоинт для получения профиля пользователя по id
def profile(username: str,
            token: str = Depends(oauth2_scheme),
            session: Session = Depends(get_db)):
    # Зависимость для получения сессии базы данных
    """
    Этот эндпоинт обрабатывает запрос на получение профиля пользователя по его идентификатору.
    Он принимает идентификатор пользователя в качестве входных данных и использует его для получения данных пользователя
    из базы данных.
    Затем он возвращает данные пользователя.
    """
    return user_db_services.get_user(session=session, user_name=username)  # Возвращаем данные пользователя по id


@app.get("/stories/{story_id}", response_model=StoryCreateSchema)  # Эндпоинт для получения истории по id
def read_story(story_id: int, db: Session = Depends(get_db)):  # Зависимость для получения сессии базы данных
    """
    Этот эндпоинт обрабатывает запрос на получение истории по ее идентификатору.
    Он принимает идентификатор истории в качестве входных данных и использует его для получения истории из базы данных.
    Если история не найдена, он возвращает ошибку 404.
    Если история найдена, он возвращает данные истории.
    """
    story = get_story_by_id(db, story_id=story_id)  # Получаем историю по id
    if story is None:
        raise HTTPException(status_code=404, detail="История не найдена")
        # Если история не найдена, возвращаем ошибку 404
    return story  # Возвращаем данные истории


# Пока не работает
@app.get("/users/{username}/stories_by_username", response_model=StoryCreateSchema)
# Эндпоинт для получения всех историй пользователя по username
def read_user_stories(username: str, db: Session = Depends(get_db)):  # Зависимость для получения сессии базы данных
    """
    Этот эндпоинт обрабатывает запрос на получение всех историй пользователя по его имени пользователя.
    Он принимает имя пользователя в качестве входных данных и использует его для получения пользователя из базы данных.
    Если пользователь не найден, он возвращает ошибку 404.
    Если пользователь найден, он получает все истории этого пользователя и возвращает их.
    """
    user = get_user(db, user_name=username)  # Получаем пользователя по username
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
        # Если пользователь не найден, возвращаем ошибку 404
    stories = get_all_user_stories(db, user_id=user.id)  # Получаем все истории пользователя
    return stories  # Возвращаем истории пользователя


@app.post("/stories", response_model=StoryCreateSchema)  # Эндпоинт для создания истории
def create_story_endpoint(story: StoryCreateSchema,
                          token: str = Depends(oauth2_scheme),
                          db: Session = Depends(get_db)):


    # Зависимость для получения сессии базы данных
    """
    Этот эндпоинт обрабатывает запрос на создание новой истории.
    Он принимает данные истории в качестве входных данных и использует их для создания новой истории в базе данных.
    Затем он возвращает данные созданной истории.
    """
    return create_story(session=db, story=story)
    # Создаем историю и возвращаем ее данные


@app.post("/goals", response_model=GoalBase)  # Эндпоинт для создания истории
def create_story_endpoint(goal: GoalBase,
                          token: str = Depends(oauth2_scheme),
                          db: Session = Depends(get_db)):


    # Зависимость для получения сессии базы данных
    """
    Этот эндпоинт обрабатывает запрос на создание новой истории.
    Он принимает данные истории в качестве входных данных и использует их для создания новой истории в базе данных.
    Затем он возвращает данные созданной истории.
    """
    return create_goal(session=db, goal=goal)


#@app.get("/kolvo likes")


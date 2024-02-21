import fastapi
from fastapi import Depends, Body, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from Models import user as user_model
from Schemas.user import UserCreateSchema, UserSchema, UserLoginSchema
from database_initializer import get_db
from Services.database import user as user_db_services
from typing import Dict
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = fastapi.FastAPI()


@app.post('/login', response_model=Dict)
def login(
        payload: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_db)
):
    """Processes user's authentication and returns a token
    on successful authentication.

    request body:

    - username: Unique identifier for a user e.g email, 
                phone number, name

    - password:
    """
    try:
        user: user_model.User = user_db_services.get_user(
            session=session, email=payload.username
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid user credentials"
        )

    is_validated: bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid user credentials"
        )
    return user.generate_token()


@app.post("/signup", response_model=UserSchema)
def signup(
        payload: UserCreateSchema = Body(),
        session: Session = Depends(get_db)
):
    """Обрабатывает запрос на регистрацию учетной записи пользователя."""
    payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
    return user_db_services.create_user(session, user=payload)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.get("/profile/{id}", response_model=UserSchema)
def profile(
        id: int,
        token: str = Depends(oauth2_scheme),
        session: Session = Depends(get_db)):
    """Обрабатывает запрос на получение профиля пользователя
    по идентификатору
    """
    return user_db_services.get_user_by_id(session=session, id=id)

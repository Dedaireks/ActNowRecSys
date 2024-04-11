from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from Schemas.user import UserSchema, UserCreateSchema, UserBaseSchema, UserChangeSchema
from Services.database.user import get_user
from database_initializer import get_db
from Services.database import user as user_db_services
from Models import user as user_model


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


#  Работает
@router.post("/signup", response_model=UserSchema)
def signup(
        payload: UserCreateSchema = Body(),
        session: Session = Depends(get_db)
):
    payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
    return user_db_services.create_user(session, user=payload)


#  Работает
@router.get("/profile/{username}", response_model=UserSchema)
def profile(username: str,
            session: Session = Depends(get_db)):
    return user_db_services.get_user(session=session, user_name=username)


@router.patch("/update/{username}")
def update_user(username: str,
                userscheme: UserChangeSchema,
                db: Session = Depends(get_db),
                token: str = Depends(oauth2_scheme)):
    user = get_user(db, user_name=username)
    current_user = user_model.User.get_current_user_by_token(token)
    current_user_id = current_user["id"]
    if user.id != current_user_id:
        raise HTTPException(status_code=403, detail="Вы не имеете прав на изменение этого пользователя")
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    user_db_services.change_user(session=db, username=username, user=userscheme)
    return {"Данные пользователя изменены"}

# def update_user(
#         payload: UserBaseSchema,
#         db: Session = Depends(get_db),
#         token: str = Depends(oauth2_scheme)):
#     return user_db_services.change_user(session=db, user=payload)


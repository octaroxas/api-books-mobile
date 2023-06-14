from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger

from api.gateway.database import DatabaseGateway
from api.controller.auth import AuthController
from api.controller.user import UserController
from api.model.user import Token, DBUser, CreatedUser, RemovedUser

methods_meta = [
    {
        "name": "Users",
        "description": "Section dedicated for Users Management.",
    },
    {
        "name": "Books",
        "description": "Section dedicated for Books Management."
    },
    {
        "name": "Debug",
        "description": "Section dedicated for endpoints with debugging purposes."
    }
]

with open("docs/API_DESC.md", "r") as desc:
    description = desc.read()

app = FastAPI(
    title="Égua, onde eu tava?",
    version="0.1.6",
    contact={
        "name": "Lucas Darlindo Freitas Rodrigues",
        "url": "https://www.linkedin.com/in/lucasdfr/",
        "email": "lucas.darlindo@gmail.com"
    },
    docs_url=None, redoc_url="/documentation",
    openapi_tags=methods_meta, description=description
)


@app.get(path="/debug/database", tags=["Debug"])
def test_database_connection() -> bool:
    try:
        DatabaseGateway()
        return True
    except Exception as e:
        logger.error(f"Database connection error. Error/Exception: {e}.")
        return False


@app.post(path="/users/auth", response_model=Token, tags=["Users"])
async def user_login(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()]) -> dict:
    user = AuthController().authenticate_user(
        username=user_credentials.username, password=user_credentials.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = AuthController().create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer", "expiration_time": None}


@app.put(path="/users/create", tags=["Users"], response_model=CreatedUser)
async def create_user(user_data: DBUser) -> dict:
    insertion_status = AuthController().insert_user(user_data=user_data)
    if insertion_status:
        return {"username": user_data.nickname, "status": "acknowledged"}
    else:
        return {"username": user_data.nickname, "status": "error"}


@app.delete(path="/users/delete/{user_id}", tags=["Users"], response_model=RemovedUser)
async def remove_user(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()], user_id: int) -> dict:
    logger.debug(user_credentials.username)

    delete_status = UserController().delete_user(user_id=user_id)
    return delete_status

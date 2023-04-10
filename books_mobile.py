from typing import Annotated

from starlette.requests import Request
from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger

from api.gateway.database import DatabaseAPI
from api.controller.auth import BooksAuthController
from api.model.user import Token

methods_meta = [
    {
        "name": "Authentication",
        "description": "Section dedicated for Authentication.",
    },
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
    title="Égua, onde eu tava",
    version="0.1.0",
    contact={
        "name": "Lucas Darlindo Freitas Rodrigues",
        "url": "https://www.linkedin.com/in/lucasdfr/",
        "email": "lucas.darlindo@gmail.com"
    },
    docs_url=None, redoc_url="/documentation",
    openapi_tags=methods_meta, description=description
)


@app.get(path="/test-dbcx", tags=["Debug"])
def test_database_connection() -> bool:
    try:
        DatabaseAPI()
        return True
    except Exception as e:
        logger.error(f"Database connection error. Error/Exception: {e}.")
        return False


@app.post(path="/auth-user", response_model=Token, tags=["Users", "Authentication"])
async def user_login(user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = BooksAuthController().authenticate_user(
        username=user_credentials.username, password=user_credentials.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = BooksAuthController().create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer", "expiration_time": None}

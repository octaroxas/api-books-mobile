from fastapi import FastAPI
from loguru import logger

from api.gateway.database import DatabaseAPI

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

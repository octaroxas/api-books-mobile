from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

from api.model.user import *
from api.controller.user import UserController


class AuthController:
    __SECRET_KEY = "a5dc873c70bd91166280c912ee8c2c4a90b79160e643f50f026198f72d3fb3a3"
    __ALGORITHM = "HS256"
    __AUTHCTX = CryptContext(schemes=["bcrypt"], deprecated="auto")
    __AUTHSCH = OAuth2PasswordBearer(tokenUrl="/users/auth", scheme_name="JWT")
    __USRCTRL = UserController()

    def get_auth_scheme(self) -> OAuth2PasswordBearer:
        return self.__AUTHSCH

    def insert_user(self, user_data: DBUser) -> bool:
        hashed_pwd = self.get_password_hash(password=user_data.password)

        user_data.password = hashed_pwd
        return self.__USRCTRL.insert_user(user_data=user_data)

    def get_user(self, username: str) -> DBUser | None:
        if username in self.__USRCTRL.get_users():
            user_dict = self.__USRCTRL.get_users()[username]
            return DBUser(**user_dict)

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        encoded_jwt = jwt.encode(to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM)
        return encoded_jwt

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.__AUTHCTX.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.__AUTHCTX.hash(password)

    def authenticate_user(self, username: str, password: str) -> bool | DBUser:
        user_data = self.get_user(username)
        if not user_data:
            return False
        if not self.verify_password(password, user_data.password):
            return False
        return user_data

    async def get_current_user(self, token: str = Depends(__AUTHSCH)) -> DBUser | None:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.__SECRET_KEY, algorithms=[self.__ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user_data = self.get_user(username=token_data.username)
        if user_data is None:
            raise credentials_exception
        return user_data

    @staticmethod
    async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
        return current_user

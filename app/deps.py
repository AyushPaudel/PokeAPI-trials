from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from core.model import Users
from auth import verify_token_access
from services.database import get_db


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="api/v1/user/login",

)


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: AsyncSession = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_email = verify_token_access(token, credentials_exception)

    query = select(Users).where(Users.email == user_email)
    result = await session.execute(query)
    try:
        result.scalar_one()
    except NoResultFound:
        raise credentials_exception

    return user_email


CURR_USER = Annotated[Users, Depends(get_current_user)]
DBSession = Annotated[AsyncSession, Depends(get_db)]

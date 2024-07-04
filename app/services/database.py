from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (AsyncConnection, AsyncEngine,
                                    async_sessionmaker, create_async_engine)

from services.config import settings


class DatabaseSessionManager:
    def __init__(self, host: str):
        self._engine: AsyncEngine | None = create_async_engine(host, echo=True)
        self._sessionmaker: async_sessionmaker | None = async_sessionmaker(
            autocommit=False, bind=self._engine
        )

    def init(self, host: str):
        self._engine = create_async_engine(host)
        self._sessionmaker = async_sessionmaker(autocommit=False, bind=self._engine)

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager isn't initialized")
        await self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager isn't initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncConnection]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager isn't initialized")

        session = self._sessionmaker()

        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

session_manager = DatabaseSessionManager(host=settings.DATABASE_URL)


async def get_db():
    async with session_manager.session() as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    if session_manager._engine is not None:
        # Close the DB Connection
        await session_manager.close()

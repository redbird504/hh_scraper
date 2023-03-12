from typing import Type, Callable
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.base import BaseRepository
from app.db.session import async_session


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
        await session.commit()


def get_repository(
    repo_type: Type[BaseRepository],
) -> Callable[[AsyncSession], BaseRepository]:
    def _wrap(session: AsyncSession = Depends(get_session)) -> BaseRepository:
        return repo_type(session)
    return _wrap

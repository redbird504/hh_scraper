from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


__all__ = ("get_session",)


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/sqlalchemy_learn",

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(engine, expire_on_commit=False, autoflush=True,
                             class_=AsyncSession)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

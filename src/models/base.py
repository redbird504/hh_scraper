from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import inspect


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    def to_dict(self) -> dict:
        return {attr.key: attr.value for attr in inspect(self).attrs}

from sqlalchemy import String
from app.db.base import Base

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Candidate(Base):
    __tablename__ = "candidates"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    middle_name: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    education: Mapped[str] = mapped_column(String, nullable=True)
    work_experience: Mapped[str] = mapped_column(String, nullable=True)

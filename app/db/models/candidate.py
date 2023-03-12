from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped

from app.db.models.base import Base


class Candidate(Base):
    __tablename__ = "candidates"
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    middle_name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    education: Mapped[str] = mapped_column(nullable=True)
    work_experience: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self):
        return f"Candidate (id={self.id})"

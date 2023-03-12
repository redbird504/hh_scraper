from typing import Optional
from pydantic import BaseModel


class Education(BaseModel):
    year: str
    university: str

    def __str__(self):
        return f"{self.year} - {self.university}"


class WorkExperience(BaseModel):
    year: str
    experience: str

    def __str__(self):
        return f"{self.year} - {self.experience}"


class HhResume(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    education: list[Education]
    work_experience: list[WorkExperience]

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
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    email: str | None
    phone: str | None
    education: list[Education]
    work_experience: list[WorkExperience]

from pydantic import BaseModel


class Candidate(BaseModel):
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    email: str | None
    education: str | None
    work_experience: str | None

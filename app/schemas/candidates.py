from pydantic import BaseModel, HttpUrl


class CandidateUrl(BaseModel):
    url: HttpUrl


class CandidateInCreate(BaseModel):
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    phone: str | None
    email: str | None
    education: str | None
    work_experience: str | None


class CandidateInUpdate(CandidateInCreate):
    ...


class CandidateForResponse(CandidateInCreate):
    id: int

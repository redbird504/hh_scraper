from pydantic import BaseModel, HttpUrl


class CandidateLoadSchema(BaseModel):
    url: HttpUrl


class CandidateBaseSchema(BaseModel):
    first_name: str | None
    last_name: str | None
    middle_name: str | None
    phone: str | None
    email: str | None
    education: str | None
    work_experience: str | None


class CandidateSchema(CandidateBaseSchema):
    id: int

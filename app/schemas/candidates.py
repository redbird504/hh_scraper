from typing import Optional
from pydantic import BaseModel, HttpUrl


class CandidateUrl(BaseModel):
    url: HttpUrl


class CandidateInCreate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    education: Optional[str]
    work_experience: Optional[str]


class CandidateInUpdate(CandidateInCreate):
    ...


class CandidateForResponse(CandidateInCreate):
    id: int

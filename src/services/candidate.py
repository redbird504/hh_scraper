import httpx
from src.clients import hh_client
from src.clients import HhClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from fastapi import Depends
from src.database import get_session
from src.schemas.candidates import CandidateSchema, CandidateBaseSchema
from src.models.candidate import Candidate
from fastapi import HTTPException


class CandidateService:
    def __init__(self, client: HhClient, session: AsyncSession) -> None:
        self._client = client
        self._session = session

    async def load_candidate(self, url: str):
        try:
            result = await self._client.get_resume(url)
        except httpx.HTTPStatusError as error:
            raise HTTPException(status_code=403, detail=str(error))
        return result 

    async def create_candidate(self, candidate: CandidateBaseSchema):
        new_candidate = Candidate(**candidate.dict())
        self._session.add(new_candidate)
        await self._session.commit()
        return CandidateSchema(**new_candidate.to_dict())

    async def get_candidate(self, candidate_id: int):
        candidate = await self._session.get(Candidate, candidate_id)
        return CandidateSchema(**candidate.to_dict())

    async def get_candidates(self) -> list[CandidateSchema]:
        candidates: list[Candidate] = await self._session.scalars(select(Candidate))
        return [CandidateSchema(**candidate.to_dict()) for candidate in candidates]

    async def update_candidate(self, candidate_id, candidate: CandidateBaseSchema):
        result = await self._session.execute(
            update(Candidate)
            .values(candidate.dict())
            .where(Candidate.id==candidate_id)
        )
        await self._session.commit()
        obj = await self._session.get(Candidate, candidate_id)        
        return CandidateSchema(**obj.to_dict())

def get_candidate_service(session: AsyncSession = Depends(get_session)) -> CandidateService:
    return CandidateService(
        hh_client,
        session
    )

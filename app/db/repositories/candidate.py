from sqlalchemy import delete, select, update
from app.db.models.candidate import Candidate
from app.db.repositories.base import BaseRepository
from app.schemas.candidates import (
    CandidateInCreate,
    CandidateInUpdate,
    CandidateForResponse
)


class CandidatesRepository(BaseRepository):
    async def create_candidate(
        self,
        candidate: CandidateInCreate
    ) -> CandidateForResponse:
        new_candidate = Candidate(**candidate.dict())
        self._session.add(new_candidate)
        return CandidateForResponse(**new_candidate.to_dict())

    async def get_candidate_by_id(self, id: int) -> CandidateForResponse:
        candidate = await self._session.get(Candidate, id)
        return CandidateForResponse(**candidate.to_dict())

    async def get_candidates(self) -> list[CandidateForResponse]:
        candidates: list[Candidate] = await self._session.scalars(
            select(Candidate)
            )
        return [
            CandidateForResponse(**candidate.to_dict())
            for candidate in candidates
        ]

    async def update_candidate(
        self,
        id: int,
        candidate: CandidateInUpdate
    ) -> CandidateForResponse:
        await self._session.execute(
            update(Candidate)
            .values(candidate.dict())
            .where(Candidate.id == id)
        )
        obj = await self._session.get(Candidate, id)
        return CandidateForResponse(**obj.to_dict())

    async def delete_candidate(self, id: int) -> None:
        await self._session.execute(
            delete(Candidate).
            where(Candidate.id == id)
        )

from sqlalchemy import delete, select, update

from app.db.errors import EntityDoesNotExist
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
        return new_candidate

    async def get_candidate(self, id: int) -> CandidateForResponse:
        candidate = await self._session.get(Candidate, id)
        if candidate is None:
            raise EntityDoesNotExist(
                f"Candidate with id {id} doesn't exist"
            )

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
        candidate_updated = (
            await self._session.scalar(
                    update(Candidate).
                    returning(Candidate).
                    values(candidate.dict()).
                    where(Candidate.id == id)
                )
            )

        if not candidate_updated:
            raise EntityDoesNotExist(
                f"Candidate with id {id} doesn't exist"
            )

        return CandidateForResponse(**candidate_updated.to_dict())

    async def delete_candidate(self, id: int) -> None:
        candidate = (
            await self._session.scalar(
                    delete(Candidate).
                    returning(Candidate).
                    where(Candidate.id == id)
                )
            )

        if candidate is None:
            raise EntityDoesNotExist(
                f"Candidate with id {id} doesn't exist"
            )

        return CandidateForResponse(**candidate.to_dict())

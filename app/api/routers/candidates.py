from fastapi import APIRouter, status, Depends
from app.api.dependencies.clients import get_hh_client

from app.api.dependencies.db import get_repository
from app.clients.hh_client import HhClient
from app.clients.schemas import HhResume
from app.db.repositories.candidate import CandidatesRepository
from app.schemas.candidates import (
    CandidateInCreate,
    CandidateInUpdate,
    CandidateForResponse,
    CandidateUrl
)


router = APIRouter(
    prefix="/candidates",
    tags=["candidates"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)


@router.get(
    "/",
    response_model=list[CandidateForResponse],
    status_code=status.HTTP_200_OK,
)
async def get_candidates(
    candidates_repo: CandidatesRepository = Depends(
        get_repository(CandidatesRepository)
    )
):
    return await candidates_repo.get_candidates()


@router.post(
    "/",
    response_model=CandidateInCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_candidate(
    candidate: CandidateInCreate,
    candidates_repo: CandidatesRepository = Depends(
        get_repository(CandidatesRepository)
    )
):
    return await candidates_repo.create_candidate(candidate)


@router.get(
    "/{candidate_id}",
    response_model=CandidateForResponse,
    status_code=status.HTTP_200_OK,
)
async def get_candidate(
    candidate_id: int,
    candidates_repo: CandidatesRepository = Depends(
        get_repository(CandidatesRepository)
    )
):
    return await candidates_repo.get_candidate(candidate_id)


@router.post(
    "/load",
    response_model=HhResume,
    status_code=status.HTTP_200_OK,
)
async def load_candidate(
    url: CandidateUrl,
    hh_client: HhClient = Depends(get_hh_client)
):
    return await hh_client.get_resume(url.url)


@router.put(
    "/{candidate_id}",
    response_model=CandidateForResponse,
    status_code=status.HTTP_200_OK,
)
async def update_candidate(
    candidate_id: int,
    candidate: CandidateInUpdate,
    candidates_repo: CandidatesRepository = Depends(
        get_repository(CandidatesRepository)
    )
):
    return await candidates_repo.update_candidate(candidate_id, candidate)


@router.delete(
    "/{candidate_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_candidate(
    candidate_id: int,
    candidates_repo: CandidatesRepository = Depends(
        get_repository(CandidatesRepository)
    )
):
    return await candidates_repo.delete_candidate(candidate_id)

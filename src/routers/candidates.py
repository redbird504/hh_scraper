from fastapi import APIRouter, status, Depends
from src.schemas.candidates import CandidateLoadSchema, CandidateBaseSchema
from src.services.candidate import CandidateService, get_candidate_service

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"],
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def get_candidates(
    candidate_services: CandidateService = Depends(get_candidate_service)
):
    return await candidate_services.get_candidates()


@router.post("/")
async def create_candidate(
    candidate: CandidateBaseSchema,
    candidate_services: CandidateService = Depends(get_candidate_service)
):
    return await candidate_services.create_candidate(candidate)


@router.get("/{candidate_id}")
async def get_candidate(
    candidate_id: int,
    candidate_services: CandidateService = Depends(get_candidate_service)
):
    return await candidate_services.get_candidate(candidate_id)


@router.post("/load")
async def load_candidate(
    url: CandidateLoadSchema,
    candidate_services: CandidateService = Depends(get_candidate_service)
):
    return await candidate_services.load_candidate(url.url)


@router.put("/{candidate_id}")
async def update_candidate(
    candidate_id: int,
    candidate: CandidateBaseSchema,
    candidate_services: CandidateService = Depends(get_candidate_service)
):
    return await candidate_services.update_candidate(candidate_id, candidate)

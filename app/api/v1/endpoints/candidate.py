from fastapi import APIRouter
from app.schemas.candidate import Candidate


router = APIRouter()


@router.get("/{candidate_id}", status_code=200, response_model=Candidate)
async def get_candidate(candidate_id: int):
    pass


@router.post("/", status_code=201, response_model=Candidate)
async def create_candidate(candidate: Candidate):
    pass


@router.post('/load/', status_code=200, response_model=Candidate)
async def load_candidate():
    pass


@router.put("/{candidate_id}", status_code=200, response_model=Candidate)
async def update_candidate(candidate_id: int):
    pass


@router.delete("/{candidate_id}", status_code=200, response_model=Candidate)
async def delete_candidate(candidate_id: int):
    pass

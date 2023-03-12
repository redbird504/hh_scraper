from fastapi import APIRouter
from src.routers import candidates


api_router = APIRouter()
api_router.include_router(candidates.router)

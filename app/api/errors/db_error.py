from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi import status
from app.db.errors import EntityDoesNotExist


async def db_error_handler(_: Request, exc: EntityDoesNotExist) -> JSONResponse:
    return JSONResponse({"errors": [str(exc)]}, status_code=status.HTTP_400_BAD_REQUEST)

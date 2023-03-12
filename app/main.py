from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.candidates import router
from app.core.config import settings
from app.api.errors.http_error import http_error_handler
from app.api.errors.db_error import db_error_handler
from app.db.errors import EntityDoesNotExist


def get_application() -> FastAPI:
    app = FastAPI(**settings.fastapi_kwargs)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix=settings.api_prefix)
    app.add_exception_handler(HTTPException, http_error_handler)
    app.add_exception_handler(EntityDoesNotExist, db_error_handler)

    return app


app = get_application()

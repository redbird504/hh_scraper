from fastapi import FastAPI

from app.api.routers.candidates import router
from app.core.config import settings


def get_application() -> FastAPI:
    app = FastAPI(**settings.fastapi_kwargs)
    app.include_router(router, prefix=settings.api_prefix)
    return app


app = get_application()

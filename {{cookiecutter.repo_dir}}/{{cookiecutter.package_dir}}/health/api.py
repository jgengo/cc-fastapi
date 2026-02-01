from fastapi import APIRouter

from {{cookiecutter.package_dir}}.health.api_format import GetHealthResponse


def create_health_router() -> APIRouter:
    router = APIRouter()

    @router.get("/", response_model=GetHealthResponse, tags=["Health"])
    @router.get("/health", response_model=GetHealthResponse, tags=["Health"])
    async def get_health() -> GetHealthResponse:
        return GetHealthResponse(status="OK")

    return router

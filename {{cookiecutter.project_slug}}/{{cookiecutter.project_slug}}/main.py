from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from {{cookiecutter.project_slug}}.config import Config
from {{cookiecutter.project_slug}}.health.api import create_health_router


def create_routers(config: Config) -> list[APIRouter]:
    return [
        create_health_router(),
    ]


def create_api(config: Config, do_enable_lifespan: bool = True) -> FastAPI:

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        for router in create_routers(config):
            app.include_router(router)
        yield

    app = FastAPI(
        title="{{cookiecutter.project_name}}",
        lifespan=lifespan if do_enable_lifespan else None
    )

    return app


if __name__ in {"main", "{{cookiecutter.project_slug}}.main"}:  # pargma: no cover
    app = create_api(config=Config())

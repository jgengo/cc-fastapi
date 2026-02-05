from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

{%- if cookiecutter.sentry %}
from {{cookiecutter.package_dir}}.common.clients.sentry import init_sentry
{%- endif %}
from {{cookiecutter.package_dir}}.config import Config
from {{cookiecutter.package_dir}}.health.api import create_health_router
{%- if cookiecutter.celery %}
from {{cookiecutter.package_dir}}.tasks.api import create_tasks_router
{%- endif %}


def create_routers(config: Config) -> list[APIRouter]:
    routers = [
        create_health_router(),
        {%- if cookiecutter.celery %}
        create_tasks_router(),
        {%- endif %}
    ]
    return routers


def create_api(config: Config, do_enable_lifespan: bool = True) -> FastAPI:

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        for router in create_routers(config):
            app.include_router(router)
        yield

    app = FastAPI(
        title="{{cookiecutter.project_name}}",
        description="{{cookiecutter.description}}",
        lifespan=lifespan if do_enable_lifespan else None
    )

    {%- if cookiecutter.sentry %}
    init_sentry(config)
    {%- endif %}

    return app


if __name__ in {"main", "{{cookiecutter.package_dir}}.main"}:  # pargma: no cover
    app = create_api(config=Config())

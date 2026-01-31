from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from {{cookiecutter.project_slug}}.config import Config
from {{cookiecutter.project_slug}}.health.api import create_health_router
from {{cookiecutter.project_slug}}.main import create_api


@pytest.fixture
def client() -> TestClient:
    api = create_api(config=Config())
    api.include_router(create_health_router())
    return TestClient(api)


@pytest.mark.parametrize(
    "route",
    (
        pytest.param("/", id="root"),
        pytest.param("/health", id="health"),
    ),
)
def test_get_health(client: TestClient, route: str) -> None:
    response = client.get(route)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"status": "OK"}
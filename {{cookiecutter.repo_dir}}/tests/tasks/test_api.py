from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from {{cookiecutter.package_dir}}.config import Config
from {{cookiecutter.package_dir}}.main import create_api
from {{cookiecutter.package_dir}}.tasks.api import create_tasks_router
from {{cookiecutter.package_dir}}.worker import celery


@pytest.fixture(autouse=True)
def celery_eager_mode():
    celery.conf.task_always_eager = True
    celery.conf.task_eager_propagates = True
    celery.conf.task_store_eager_result = True
    yield
    celery.conf.task_always_eager = False
    celery.conf.task_eager_propagates = False
    celery.conf.task_store_eager_result = False


@pytest.fixture
def client() -> TestClient:
    api = create_api(config=Config())
    api.include_router(create_tasks_router())
    return TestClient(api)


def test_create_task(client: TestClient) -> None:
    response = client.post("/tasks")
    content = response.json()
    task_id = content["task_id"]
    assert task_id

    response = client.get(f"tasks/{task_id}")
    content = response.json()
    assert content == {"task_id": task_id, "status": "SUCCESS", "result": True}
    assert response.status_code == HTTPStatus.OK

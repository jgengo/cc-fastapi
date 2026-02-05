from fastapi import APIRouter

from {{cookiecutter.package_dir}}.tasks.api_format import TaskCreateResponse, TaskStatusResponse
from {{cookiecutter.package_dir}}.worker import new_task


def create_tasks_router() -> APIRouter:
    router = APIRouter()

    @router.post("/tasks", response_model=TaskCreateResponse)
    async def create_task() -> TaskCreateResponse:
        task = new_task.delay()
        return TaskCreateResponse(task_id=task.id)

    @router.get("/tasks/{task_id}", response_model=TaskStatusResponse)
    async def get_task(task_id: str) -> TaskStatusResponse:
        task = new_task.AsyncResult(task_id)

        return TaskStatusResponse(task_id=task_id, status=task.state, result=task.result)

    return router

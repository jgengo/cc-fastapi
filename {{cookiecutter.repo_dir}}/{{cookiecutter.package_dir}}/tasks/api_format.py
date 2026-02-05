from typing import Any

from pydantic import BaseModel


class TaskCreateResponse(BaseModel):
    task_id: str


class TaskStatusResponse(BaseModel):
    task_id: str
    status: str
    result: Any | None = None
import time

from celery import Celery
from {{cookiecutter.package_dir}}.config import Config

config = Config()

celery = Celery(__name__)
celery.conf.broker_url = config.redis_url
celery.conf.result_backend = config.redis_url


@celery.task(name="new_task")
def new_task() -> bool:
    time.sleep(5)
    return True
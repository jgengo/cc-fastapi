import sentry_sdk
from fastapi import HTTPException
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

from {{cookiecutter.package_dir}}.config import Config


def init_sentry(config: Config) -> None:
    if config.enable_sentry:
        sentry_sdk.init(
            dsn=config.sentry_dsn,
            environment=config.env.value,
            send_default_pii=True,
            integrations=[FastApiIntegration(), StarletteIntegration()],
            ignore_errors=[HTTPException]
        )

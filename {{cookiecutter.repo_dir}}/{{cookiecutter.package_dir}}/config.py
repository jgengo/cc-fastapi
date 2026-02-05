from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvEnum(str, Enum):
    LOCAL = "local"
    DEVELOPMENT = "development"
    TEST = "test"
    PRODUCTION = "production"


class Config(BaseSettings):
    env: EnvEnum

    {%- if cookiecutter.sentry %}
    enable_sentry: bool = False
    sentry_dsn: str
    {%- endif %}

    {%- if cookiecutter.celery %}
    redis_url: str = "redis://localhost:6379/0"
    {%- endif %}

    def env_is_prod(self) -> bool:
        return self.env == EnvEnum.PRODUCTION

    def env_is_dev(self) -> bool:
        return self.env == EnvEnum.DEVELOPMENT

    def env_is_local(self) -> bool:
        return self.env == EnvEnum.LOCAL

    def env_is_test(self) -> bool:
        return self.env == EnvEnum.TEST

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

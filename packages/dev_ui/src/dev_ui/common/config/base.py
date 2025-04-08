from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="ui_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    backend_url: str

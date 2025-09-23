from functools import lru_cache
import os


class Settings:
    """轻量 Settings，直接从环境变量读取以避免对 pydantic 的运行时依赖。

    这是一个短期兼容实现：当需要更复杂的类型校验或 env_file 支持时，
    可改回使用 pydantic-settings / BaseSettings 并在 pyproject.toml 中添加相应依赖。
    """

    def __init__(self) -> None:
        self.ENVIRONMENT: str = os.getenv("ENVIRONMENT", "dev")
        self.APP_NAME: str = os.getenv("APP_NAME", "Educative Service")
        # self.DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

    def dict(self):
        return {
            "ENVIRONMENT": self.ENVIRONMENT,
            "APP_NAME": self.APP_NAME,
        }


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

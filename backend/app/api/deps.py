# 预留放置依赖注入函数，例如获取DB Session、当前用户等
from typing import Generator


def get_db() -> Generator:  # placeholder
    # with SessionLocal() as session:
    #     yield session
    yield None

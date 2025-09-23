from fastapi import FastAPI
from .core.config import settings
from .api.routes import health, demo, auth
from .db import init_db


app = FastAPI(title="Educative Service", version="0.1.0")

# 初始化数据库（创建表）
init_db()

# Include routers
app.include_router(health.router, prefix="/api")
app.include_router(demo.router, prefix="/api")
app.include_router(auth.router, prefix="/api")


@app.get("/")
async def root():
    return {"service": "educative", "environment": settings.ENVIRONMENT}

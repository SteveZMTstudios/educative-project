# Backend (FastAPI)

## Quick Start

1. 安装 Poetry (如果未安装)
2. 安装依赖:
```
poetry install
```
3. 运行开发服务器:
```
poetry run uvicorn app.main:app --reload --port 8000
```
4. 打开: http://127.0.0.1:8000/docs 查看自动接口文档

## 结构说明
```
backend/
  pyproject.toml
  app/
    main.py            # 入口
    core/config.py     # 配置 & 环境变量
    api/deps.py        # 依赖注入 (数据库/认证等预留)
    api/routes/
      __init__.py
      health.py        # 健康检查
      demo.py          # 示例业务
```

后续可扩展 modules: users, auth, exercises, matchmaking 等。

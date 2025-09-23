# Educative Project 平台骨架

该仓库提供一个初始的全栈（Vue3 + FastAPI）可扩展教学 / 练习 / 匹配服务框架。

## 技术栈选择说明
- 前端: Vue 3 + Vite + TypeScript
  - 轻量快速，生态成熟，适合中台与交互式练习界面
- 后端: FastAPI (Python)
  - 高性能、类型友好、内建交互式文档 (Swagger / ReDoc)
  - 便于快速迭代与后续扩展（账号、练习、匹配、推荐）
- 包管理: 前端 npm, 后端 Poetry
- 接口风格: REST (可视需要后续补充 WebSocket 用于实时协作 / 匹配状态推送)

## 项目结构
```
backend/        # FastAPI 应用
frontend/       # Vue3 前端 (Vite)
docs/           # 规划与技术文档
```

## 快速开始
### 启动后端
```
cd backend
poetry install
poetry run uvicorn app.main:app --reload --port 8000
```
访问: http://127.0.0.1:8000/docs (Swagger UI)

### 启动前端
```
cd frontend
npm install
npm run dev
```
访问: http://127.0.0.1:5173

前端通过代理访问后端 /api/*。

## 下一步推荐迭代路线
1. 账号与身份
   - 路由: /api/auth/login /register /me
   - JWT + Refresh 或 Session + Redis
2. 练习题与内容
   - 题目模型: id, title, type(shell/sql/code), difficulty, tags, content, solution
   - CRUD + 列表分页 + 搜索过滤
3. 用户偏好与匹配 (best_match 文档落地)
   - 匹配算法模块 (可抽象 service/matcher.py)
   - 定时或事件驱动计算
4. 运行/判题执行沙箱 (针对 shell / 代码题)
   - 独立微服务或本地受限容器 (后期)
5. Observability & Infra
   - 日志结构化 loguru
   - 健康检查 /metrics (Prometheus) + tracing (OpenTelemetry)
6. 测试 & CI
   - GitHub Actions: 后端 pytest + ruff
   - 前端 eslint + type-check + vitest (后加)

## 环境变量
在 backend/ 下创建 .env:
```
ENVIRONMENT=dev
# DATABASE_URL=postgresql+psycopg://user:pass@localhost:5432/educative
```

## 代码风格
- 后端: Ruff + Black
- 前端: ESLint + TypeScript 严格模式

## 安全预留
- CORS 策略 (FastAPI 中间件)
- 速率限制 (待加入: slowapi 或自建中间件)
- 输入校验：Pydantic 模型

## 贡献流程
- feature/ 分支开发 -> PR -> 代码评审 -> 合并 main

欢迎继续补充 docs/ 中的业务与技术细节，将文档与实现保持同步。

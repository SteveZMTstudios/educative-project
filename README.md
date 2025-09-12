# EDUCATIVE-PROJECT
这是一个“智能技术赋能个性化学习”交互式课件平台骨架，包含前端（Vue + Vite）、后端（Node/Express）与一个 Python 推荐服务占位（Flask）。

## 本仓库结构（简要）
- `frontend/` - Vite + Vue3 前端应用（开发服务器: 5173）
- `backend/` - Node.js (Express) 后端 API（运行端口: 3000）
- `python_service/` - Flask 推荐服务占位（运行端口: 5001）

## 本地部署（PowerShell）

1) 启动后端（Express）

```powershell
cd e:\Project\educative-project\backend
npm install
# 直接运行
node index.js
# 或者开发模式（nodemon）
npm run dev
```

2) 启动 Python 推荐服务（可选，用于后端代理）

```powershell
cd e:\Project\educative-project\python_service
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

3) 启动前端（Vite）

```powershell
cd e:\Project\educative-project\frontend
npm install
npm run dev
# 在浏览器打开 http://localhost:5173/
```

注意：启动 `npm run dev` 时必须在 `frontend` 子目录执行，否则会出现 `ENOENT: no such file or directory, open '...\package.json'` 错误。

## Vite Proxy（开发模式）
前端开发配置中已包含代理（`frontend/vite.config.mjs`），把 `/api` 转发到 `http://localhost:3000`，开发时可直接从前端调用 `/api/*` 而无需处理 CORS。

验证代理：

```powershell
# 如果 Vite 已启动
Invoke-RestMethod http://localhost:5173/api/recommend | ConvertTo-Json -Depth 5
```

如果返回后端推荐数据则代理配置生效。

## 常见故障与排查
- 错误: "Install @vitejs/plugin-vue" 或 ESM 相关错误：
	- 解决：确保 `@vitejs/plugin-vue` 安装在 `frontend/node_modules` 中，并使用 `vite.config.mjs`（ESM），`frontend/package.json` 必须包含 `"type":"module"`，删除残留的 `vite.config.js`。
- 错误: `EADDRINUSE: address already in use :::3000`：
	- 说明：端口 3000 被占用。执行 `Get-NetTCPConnection -LocalPort 3000` 或 `netstat -ano | Select-String 3000` 查找 PID，并用 `Stop-Process -Id <PID>` 终止进程。
- 错误: `ENOENT: no such file or directory, open '...\package.json'`：
	- 说明：当前工作目录错误。请在包含 `package.json` 的目录执行 npm 脚本。

## 完善计划（短期优先级）
1. 完善前端页面：把所有占位内容迁移为 Vue 组件，支持移动端适配与无障碍（已开始）。
2. 身份认证：实现真实注册/登录（JWT）与 role 区分（学生/教师）。
3. 推荐引擎：把后端 `/api/recommend` 与 `python_service` 对接，支持基于学习偏好的推荐。
4. 作业/批改：实现教师发布、学生提交、自动/手动批改与成绩排名推送。
5. 测试与 CI：添加 Vitest/Playwright 测试与 GitHub Actions 自动化构建。

## 我可以帮你做（可直接执行）
- 终止占用 3000 端口的进程并重启后端。  
- 在本地通过 Vite proxy 做端到端验证。  
- 为前端添加更多组件与样式。  

如果你需要我现在代为执行其中一项，请回复对应操作，例如："结束占用端口并重启后端" 或 "验证 proxy"。



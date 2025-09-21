# 变更记录（快速迭代）

以下为本次开发会话中添加/修改的内容（最小可用实现，演示用）：

1. 后端（`backend/index.js`）
   - 添加内存用户存储 `users`, `sessions` 和 `assignments`。
   - 新增接口：
     - `POST /api/auth/register` 注册（body: {username, password, role})
     - `POST /api/auth/login` 登录（body: {username, password}) -> 返回 token
     - `POST /api/assignments` 教师发布作业（需 Authorization: Bearer <token>）
     - `GET /api/assignments` 获取作业列表（需 Authorization）
   - 保留 `GET /api/recommend` 作为占位。

2. 前端
   - 新增 `frontend/src/views/Register.vue`，实现注册页面。
   - 修改 `frontend/src/views/Login.vue` 使用新的登录接口并支持密码字段。
   - 修改 `frontend/src/views/Teacher.vue` 添加发布作业表单和查看已发布作业的逻辑（最小实现）。
   - 修改路由 `frontend/src/router/index.js` 添加 `/register` 路由。

3. 测试与验证
   - 在本地用 PowerShell 验证了注册/登录/发布/获取作业的基本流程。

注意与后续改进建议：
- 当前实现使用内存存储，仅用于开发演示；上线必须替换为持久化存储（MySQL / SQLite / Postgres）。
- 当前 token 为随机字符串存储在内存 session 中；建议使用 JWT 并设置过期时间与刷新策略。
- 应添加输入校验（后端与前端），密码应使用哈希（bcrypt）存储。
- 需要实现用户注册邮件验证、错误处理与日志记录。
- 学生提交、教师打分、课程/班级管理等功能尚未实现；可在下一阶段添加。

总体：本次更改提供了一个最小可用的认证与作业 API，并在前端提供了相应的 UI，便于后续扩展为完整系统。

# frontend

本目录为项目前端（Vite + Vue3）。

新增功能（客户端实现）：

- 课程中心（`/courses`）：浏览、按标签筛选、教师添加课程并保存在 localStorage（键：`edu_courses`）。
- 偏好选择（`/favor`）：选择兴趣标签会保存到 localStorage（键：`edu_user_prefer_tags`）。
- 学生侧推荐：点击“加载推荐”时优先请求后端 `/api/recommend`，若后端不可用则使用客户端基于标签的简单推荐（按标签交集计分）。

快速试用：

1. 在浏览器打开前端开发服务器（参见主仓库 README）。
2. 访问 `#/courses` 浏览或添加课程；添加后其他页面会读取它们。
3. 访问 `#/favor` 选择兴趣标签（例如 `python`），然后到 `#/student` 点击“加载推荐”查看基于标签的推荐。

说明：客户端推荐为占位实现，后端可实现更复杂的召回/排序并返回 `recommendations` 数组。

示例课程文档：
- 教师示例课程放在 `docs/course-examples/linux-shell-basic.md`，这是一个 "Linux Shell 基础" 的完整示例，包含章节、练习与脚本示例，可用于参考或直接导入课程中心。

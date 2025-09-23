# Frontend (Vue 3 + Vite)

## 开发启动
```
npm install
npm run dev
```
默认端口: 5173

## 代理说明
开发环境通过 Vite 代理将 /api/* 转发到 FastAPI (http://127.0.0.1:8000)。

## 目录结构
```
frontend/
  package.json
  vite.config.ts
  index.html
  tsconfig.json
  src/
    main.ts
    App.vue
```

后续计划：
- 路由管理 (Vue Router)
- 状态管理 (Pinia)
- 统一 UI 组件库 (Element Plus / Naive UI 选择其一)
- API 封装与错误处理
- 鉴权（基于 JWT / Session）

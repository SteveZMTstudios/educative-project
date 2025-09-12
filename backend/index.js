const path = require('path')
const express = require('express')
const app = express()
const port = process.env.PORT || 3000

// 静态文件
app.use('/static', express.static(path.join(__dirname, '..', 'frontend')))

// 简单 API
app.get('/api/health', (req, res) => res.json({ status: 'ok' }))

// 用户认证 stub
app.post('/api/login', express.json(), (req, res) => {
  const { username } = req.body
  if (!username) return res.status(400).json({ error: 'missing username' })
  // TODO: Replace with real auth
  res.json({ token: 'stub-token', username })
})

// 推荐接口 stub
app.get('/api/recommend', (req, res) => {
  res.json({ recommendations: [
    { id: 1, title: 'Python 入门', tag: 'python' },
    { id: 2, title: 'Linux 基础', tag: 'linux' }
  ]})
})

app.listen(port, ()=> console.log(`backend listening on ${port}`))

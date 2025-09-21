const path = require('path')
const express = require('express')
const crypto = require('crypto')
const app = express()
const port = process.env.PORT || 3000

app.use(express.json())

// 静态文件
app.use('/static', express.static(path.join(__dirname, '..', 'frontend')))

// 健康检查
app.get('/api/health', (req, res) => res.json({ status: 'ok' }))

// 简单内存存储（演示用）
const users = {} // username -> { password, role }
const sessions = {} // token -> username
const assignments = [] // { id, title, description, author }

// 注册
app.post('/api/auth/register', (req, res) => {
  const { username, password, role } = req.body || {}
  if (!username || !password) return res.status(400).json({ error: 'username and password required' })
  if (users[username]) return res.status(409).json({ error: 'user exists' })
  users[username] = { password, role: role || 'student' }
  return res.json({ ok: true, username })
})

// 登录
app.post('/api/auth/login', (req, res) => {
  const { username, password } = req.body || {}
  if (!username || !password) return res.status(400).json({ error: 'username and password required' })
  const u = users[username]
  if (!u || u.password !== password) return res.status(401).json({ error: 'invalid credentials' })
  const token = crypto.randomBytes(16).toString('hex')
  sessions[token] = username
  return res.json({ token, username, role: u.role })
})

// 中间件：简单 auth
function authMiddleware(req, res, next){
  const h = req.headers.authorization || ''
  const m = h.match(/^Bearer (.+)$/)
  if (!m) return res.status(401).json({ error: 'missing token' })
  const token = m[1]
  const username = sessions[token]
  if (!username) return res.status(401).json({ error: 'invalid token' })
  req.user = { username, ...users[username] }
  next()
}

// 发布作业（教师）
app.post('/api/assignments', authMiddleware, (req, res) => {
  if (req.user.role !== 'teacher') return res.status(403).json({ error: 'only teacher can post assignments' })
  const { title, description } = req.body || {}
  if (!title) return res.status(400).json({ error: 'title required' })
  const id = assignments.length + 1
  const a = { id, title, description: description || '', author: req.user.username }
  assignments.push(a)
  return res.json({ ok: true, assignment: a })
})

// 获取作业（学生或教师）
app.get('/api/assignments', authMiddleware, (req, res) => {
  return res.json({ assignments })
})

// 推荐接口 stub
app.get('/api/recommend', (req, res) => {
  res.json({ recommendations: [
    { id: 1, title: 'Python 入门', tag: 'python' },
    { id: 2, title: 'Linux 基础', tag: 'linux' }
  ]})
})

app.listen(port, ()=> console.log(`backend listening on ${port}`))

# Linux Shell 基础（示例课程）

课程 ID: c_linux_shell

## 课程目标
- 理解 Linux Shell 的基本概念与常见命令
- 能在命令行中完成文件/目录操作、查看文件内容与进程管理的基本任务
- 能编写简单的 Shell 脚本完成批量任务

## 目标读者
- 想要入门 Linux 命令行与基本运维/开发环境的学生

## 课时安排
1. 简介：什么是 Shell 与终端
   - 目标：理解 Shell 的作用与常见类型（bash, zsh）
   - 练习：在终端中查看当前 Shell：echo $SHELL

2. 文件与目录操作
   - 常用命令：ls, cd, pwd, mkdir, rmdir, rm, mv, cp
   - 练习：创建目录 `practice`，在其中创建 `notes.txt` 并写入一行文本。

3. 查看与编辑文件
   - 常用命令：cat, less, head, tail, grep
   - 练习：使用 `grep` 查找包含关键字 "TODO" 的行。

4. 权限与用户
   - 常用命令：chmod, chown
   - 练习：将脚本 `run.sh` 权限设置为可执行（chmod +x run.sh）。

5. 进程与系统信息
   - 常用命令：ps, top, kill, df, free
   - 练习：列出当前用户运行的进程并筛选出包含 "node" 的行。

6. 基础 Shell 脚本
   - 内容：变量、条件语句、循环、函数、参数
   - 练习：编写 `backup.sh`，将 `~/notes` 目录压缩为 `notes-$(date +%F).tar.gz`。

## 练习示例与答案（简略）
- 练习：创建目录并写入文件
  - 命令：mkdir -p practice && echo "Hello" > practice/notes.txt

- 练习：使用 grep 查找 TODO
  - 命令：grep -n "TODO" -R .

- 练习：备份脚本（backup.sh）示例：
  ```bash
  #!/bin/bash
  src="$HOME/notes"
  dest="$HOME/backup/notes-$(date +%F).tar.gz"
  mkdir -p "$(dirname "$dest")"
  tar -czf "$dest" -C "$HOME" "notes"
  echo "Backup saved to $dest"
  ```

## 扩展资源
- Bash 官方手册
- Linux 入门教程（在线课程）

---

教师提示：此课程可扩展为交互式练习（在容器中运行真实命令），或附带练习用的输入/输出样例用于自动批改。

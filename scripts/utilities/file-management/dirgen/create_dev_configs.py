#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Development Environment Configuration Creator
创建开发环境配置文件的脚本
"""

import os
import json
from pathlib import Path
from datetime import datetime

def create_dev_configs():
  """创建开发环境配置文件"""
  
  print("🔧 开始创建开发环境配置文件...")
  print("=" * 50)
  
  # VS Code 配置
  vscode_settings = {
      "editor.fontSize": 14,
      "editor.tabSize": 4,
      "editor.insertSpaces": True,
      "editor.wordWrap": "on",
      "editor.minimap.enabled": True,
      "editor.formatOnSave": True,
      "files.autoSave": "afterDelay",
      "files.autoSaveDelay": 1000,
      "workbench.colorTheme": "Dark+ (default dark)",
      "workbench.iconTheme": "vscode-icons",
      "terminal.integrated.fontSize": 12,
      "python.defaultInterpreterPath": "/usr/bin/python3",
      "python.linting.enabled": True,
      "python.linting.pylintEnabled": True,
      "git.enableSmartCommit": True,
      "git.confirmSync": False,
      "extensions.autoUpdate": True,
      "markdown.preview.fontSize": 14,
      "markdown.preview.lineHeight": 1.6
  }
  
  vscode_extensions = {
      "recommendations": [
          "ms-python.python",
          "ms-vscode.vscode-json",
          "yzhang.markdown-all-in-one",
          "shd101wyy.markdown-preview-enhanced",
          "ms-vscode.vscode-typescript-next",
          "bradlc.vscode-tailwindcss",
          "esbenp.prettier-vscode",
          "ms-vscode.vscode-eslint",
          "formulahendry.auto-rename-tag",
          "christian-kohler.path-intellisense",
          "vscode-icons-team.vscode-icons",
          "ms-vscode.theme-dark-plus",
          "github.copilot",
          "ms-vscode.live-server"
      ]
  }
  
  # Git 配置
  git_config = """[user]
  name = Your Name
  email = your.email@example.com

[core]
  editor = code --wait
  autocrlf = input
  safecrlf = true

[push]
  default = simple

[pull]
  rebase = false

[alias]
  st = status
  co = checkout
  br = branch
  ci = commit
  di = diff
  lg = log --oneline --graph --decorate --all
  last = log -1 HEAD
  unstage = reset HEAD --
  visual = !gitk

[color]
  ui = auto

[diff]
  tool = vscode

[difftool "vscode"]
  cmd = code --wait --diff $LOCAL $REMOTE

[merge]
  tool = vscode

[mergetool "vscode"]
  cmd = code --wait $MERGED
"""
  
  # Python 开发配置
  python_requirements = """# Python 开发环境依赖包
# 安装命令: pip install -r requirements.txt

# 基础工具
pip>=21.0
setuptools>=60.0
wheel>=0.37.0

# 代码质量
pylint>=2.15.0
black>=22.0.0
isort>=5.10.0
flake8>=5.0.0

# 测试工具
pytest>=7.0.0
pytest-cov>=4.0.0
coverage>=6.0.0

# 文档工具
sphinx>=5.0.0
mkdocs>=1.4.0

# 开发工具
ipython>=8.0.0
jupyter>=1.0.0
requests>=2.28.0

# Web 开发
flask>=2.2.0
fastapi>=0.85.0
django>=4.1.0

# 数据处理
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0

# 实用工具
python-dotenv>=0.21.0
click>=8.1.0
rich>=12.6.0
"""
  
  # JavaScript/Node.js 配置
  package_json = {
      "name": "personal-workspace-js",
      "version": "1.0.0",
      "description": "JavaScript development environment for personal workspace",
      "main": "index.js",
      "scripts": {
          "start": "node index.js",
          "dev": "nodemon index.js",
          "test": "jest",
          "lint": "eslint .",
          "format": "prettier --write ."
      },
      "devDependencies": {
          "eslint": "^8.0.0",
          "prettier": "^2.7.0",
          "nodemon": "^2.0.20",
          "jest": "^29.0.0"
      },
      "dependencies": {
          "express": "^4.18.0",
          "axios": "^1.1.0",
          "lodash": "^4.17.21"
      }
  }
  
  # Docker 配置
  dockerfile_python = """# Python 开发环境 Dockerfile
FROM python:3.11-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \\
  git \\
  curl \\
  vim \\
  && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["python", "app.py"]
"""
  
  docker_compose = """version: '3.8'

services:
app:
  build: .
  ports:
    - "8000:8000"
  volumes:
    - .:/app
  environment:
    - FLASK_ENV=development
    - FLASK_DEBUG=1
  depends_on:
    - db
    - redis

db:
  image: postgres:15
  environment:
    POSTGRES_DB: workspace_db
    POSTGRES_USER: workspace_user
    POSTGRES_PASSWORD: workspace_pass
  ports:
    - "5432:5432"
  volumes:
    - postgres_data:/var/lib/postgresql/data

redis:
  image: redis:7-alpine
  ports:
    - "6379:6379"

volumes:
postgres_data:
"""
  
  # 终端配置
  bash_profile = """# Personal Workspace Bash Profile
# 添加到 ~/.bashrc 或 ~/.bash_profile

# 设置环境变量
export WORKSPACE_ROOT="$HOME/personal-workspace"
export PATH="$WORKSPACE_ROOT/scripts:$PATH"

# 加载别名
if [ -f "$WORKSPACE_ROOT/scripts/aliases/bash_aliases" ]; then
  source "$WORKSPACE_ROOT/scripts/aliases/bash_aliases"
fi

# 加载自定义命令
if [ -f "$WORKSPACE_ROOT/scripts/aliases/custom_commands" ]; then
  source "$WORKSPACE_ROOT/scripts/aliases/custom_commands"
fi

# Python 环境
export PYTHONPATH="$WORKSPACE_ROOT:$PYTHONPATH"

# Node.js 环境
export NODE_PATH="$WORKSPACE_ROOT/node_modules:$NODE_PATH"

# 自定义提示符
export PS1="\\[\\033[01;32m\\]\\u@\\h\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]\\$ "

# 历史记录设置
export HISTSIZE=10000
export HISTFILESIZE=20000
export HISTCONTROL=ignoredups:erasedups

# 启动时显示工作空间信息
echo "🚀 Personal Workspace Environment Loaded"
echo "📁 Workspace: $WORKSPACE_ROOT"
echo "🛠️  Available commands: workspace, newnote, backup, searchnotes"
"""
  
  # 配置文件字典
  dev_configs = {
      "configs/development/vscode/settings.json": json.dumps(vscode_settings, indent=4),
      "configs/development/vscode/extensions.json": json.dumps(vscode_extensions, indent=4),
      "configs/development/git/gitconfig": git_config,
      "configs/development/python/requirements.txt": python_requirements,
      "configs/development/javascript/package.json": json.dumps(package_json, indent=2),
      "configs/development/docker/Dockerfile.python": dockerfile_python,
      "configs/development/docker/docker-compose.yml": docker_compose,
      "configs/development/terminal/bash_profile": bash_profile,
      
      # 环境变量文件
      "configs/system/environment/dev.env": """# 开发环境变量
# 复制到 .env 文件并修改相应值

# 数据库配置
DATABASE_URL=postgresql://workspace_user:workspace_pass@localhost:5432/workspace_db
REDIS_URL=redis://localhost:6379

# API 配置
API_BASE_URL=http://localhost:8000
API_KEY=your_api_key_here

# 调试模式
DEBUG=true
LOG_LEVEL=debug

# 第三方服务
GITHUB_TOKEN=your_github_token
OPENAI_API_KEY=your_openai_key
""",
      
      "configs/system/environment/prod.env": """# 生产环境变量
# 生产环境配置模板

# 数据库配置
DATABASE_URL=postgresql://user:pass@prod-db:5432/prod_db
REDIS_URL=redis://prod-redis:6379

# API 配置
API_BASE_URL=https://api.yourdomain.com
API_KEY=production_api_key

# 安全配置
SECRET_KEY=your_secret_key_here
JWT_SECRET=your_jwt_secret

# 调试模式
DEBUG=false
LOG_LEVEL=info

# 监控配置
SENTRY_DSN=your_sentry_dsn
""",
      
      # EditorConfig
      ".editorconfig": """# EditorConfig 配置文件
# https://editorconfig.org/

root = true

[*]
indent_style = space
indent_size = 4
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.{js,jsx,ts,tsx,json}]
indent_size = 2

[*.{yml,yaml}]
indent_size = 2

[*.md]
trim_trailing_whitespace = false

[Makefile]
indent_style = tab
""",
      
      # Prettier 配置
      "configs/development/javascript/.prettierrc": """{
"semi": true,
"trailingComma": "es5",
"singleQuote": true,
"printWidth": 80,
"tabWidth": 2,
"useTabs": false
}
""",
      
      # ESLint 配置
      "configs/development/javascript/.eslintrc.json": """{
"env": {
  "browser": true,
  "es2021": true,
  "node": true
},
"extends": [
  "eslint:recommended"
],
"parserOptions": {
  "ecmaVersion": 12,
  "sourceType": "module"
},
"rules": {
  "indent": ["error", 2],
  "linebreak-style": ["error", "unix"],
  "quotes": ["error", "single"],
  "semi": ["error", "always"]
}
}
"""
  }
  
  created_count = 0
  skipped_count = 0
  
  for file_path, content in dev_configs.items():
      path = Path(file_path)
      
      if path.exists():
          print(f"⏭️  跳过已存在的文件: {file_path}")
          skipped_count += 1
      else:
          try:
              # 确保父目录存在
              path.parent.mkdir(parents=True, exist_ok=True)
              
              with open(path, 'w', encoding='utf-8') as f:
                  f.write(content)
              
              print(f"✅ 创建配置文件: {file_path}")
              created_count += 1
              
          except Exception as e:
              print(f"❌ 创建配置文件失败 {file_path}: {e}")
  
  print("=" * 50)
  print(f"🎉 开发环境配置文件创建完成!")
  print(f"📊 统计信息:")
  print(f"   - 新创建: {created_count} 个文件")
  print(f"   - 已跳过: {skipped_count} 个文件")
  print(f"   - 总计: {len(dev_configs)} 个文件")
  
  print("\n🔧 配置说明:")
  print("   - VS Code: settings.json 和 extensions.json")
  print("   - Git: 全局配置文件")
  print("   - Python: requirements.txt 依赖文件")
  print("   - JavaScript: package.json 和代码规范配置")
  print("   - Docker: Dockerfile 和 docker-compose.yml")
  print("   - 环境变量: 开发和生产环境配置")

if __name__ == "__main__":
  try:
      create_dev_configs()
  except KeyboardInterrupt:
      print("\n\n⚠️  操作被用户中断")
  except Exception as e:
      print(f"\n❌ 发生错误: {e}")
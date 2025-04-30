#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Template Files Creator
创建模板文件的脚本
"""

import os
from pathlib import Path
from datetime import datetime

def create_template_files():
  """创建各种模板文件"""
  
  print("📝 开始创建模板文件...")
  print("=" * 50)
  
  # 模板文件内容定义
  templates = {
      # 文档模板
      "templates/documents/meeting-notes.md": """# 会议记录模板

## 会议信息
- **会议主题**: 
- **日期时间**: {date}
- **参会人员**: 
- **会议地点**: 

## 议程
1. 
2. 
3. 

## 讨论要点
### 议题1: 
- **讨论内容**: 
- **决议**: 
- **负责人**: 
- **截止时间**: 

### 议题2:
- **讨论内容**: 
- **决议**: 
- **负责人**: 
- **截止时间**: 

## 行动项
| 任务 | 负责人 | 截止时间 | 状态 |
|------|--------|----------|------|
|      |        |          |      |

## 下次会议
- **时间**: 
- **议题**: 
""",

      "templates/documents/project-plan.md": """# 项目计划模板

## 项目概述
- **项目名称**: 
- **项目描述**: 
- **项目目标**: 
- **开始日期**: {date}
- **预计结束**: 
- **项目负责人**: 

## 项目范围
### 包含内容
- 

### 不包含内容
- 

## 里程碑
| 里程碑 | 描述 | 预计完成时间 | 状态 |
|--------|------|--------------|------|
|        |      |              |      |

## 任务分解
### 阶段1: 
- [ ] 任务1
- [ ] 任务2
- [ ] 任务3

### 阶段2:
- [ ] 任务1
- [ ] 任务2

## 风险评估
| 风险 | 影响程度 | 可能性 | 应对措施 |
|------|----------|--------|----------|
|      |          |        |          |

## 资源需求
- **人力资源**: 
- **技术资源**: 
- **其他资源**: 

## 成功标准
- 
- 
- 
""",

      "templates/documents/daily-standup.md": """# 日常站会模板

## 会议信息
- **日期**: {date}
- **参会人员**: 

## 个人更新

### [姓名1]
- **昨天完成**: 
- **今天计划**: 
- **遇到问题**: 

### [姓名2] 
- **昨天完成**: 
- **今天计划**: 
- **遇到问题**: 

## 团队讨论
- 

## 行动项
- [ ] 
- [ ] 

## 备注
- 
""",

      "templates/documents/retrospective.md": """# 回顾总结模板

## 回顾信息
- **回顾周期**: 
- **日期**: {date}
- **参与人员**: 

## 做得好的地方 👍
- 
- 
- 

## 需要改进的地方 🔧
- 
- 
- 

## 遇到的问题 ⚠️
- 
- 
- 

## 行动计划 📋
| 改进项 | 负责人 | 截止时间 | 状态 |
|--------|--------|----------|------|
|        |        |          |      |

## 学到的经验 💡
- 
- 
- 

## 下次回顾
- **时间**: 
- **重点关注**: 
""",

      # 代码模板
      "templates/code/readme-template.md": """# 项目名称

## 📖 项目描述
简要描述项目的用途和功能

## 🚀 快速开始

### 环境要求
- 
- 
- 

### 安装步骤
```bash
# 克隆项目
git clone [项目地址]

# 进入项目目录
cd [项目名称]

# 安装依赖
[安装命令]
```

### 运行项目
```bash
[运行命令]
```

## 📁 项目结构
```
项目根目录/
├── src/           # 源代码
├── docs/          # 文档
├── tests/         # 测试文件
└── README.md      # 项目说明
```

## 🔧 配置说明
- 
- 

## 📚 使用文档
- 
- 

## 🤝 贡献指南
1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 📄 许可证
[许可证类型]

## 👥 维护者
- [维护者信息]

## 🙏 致谢
- 
""",
      
      # 别名文件
      "scripts/aliases/bash_aliases": """# Bash Aliases Configuration
# 个人常用 Bash 别名配置

# 基础命令增强
alias ll='ls -alF'
alias la='ls -A' 
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'

# Git 相关
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline'
alias gd='git diff'
alias gb='git branch'
alias gco='git checkout'

# 系统信息
alias df='df -h'
alias du='du -h'
alias free='free -h'
alias ps='ps aux'

# 网络相关
alias ping='ping -c 5'
alias ports='netstat -tuln'

# 开发相关
alias py='python3'
alias pip='pip3'
alias serve='python3 -m http.server'

# 自定义快捷命令
alias workspace='cd ~/personal-workspace'
alias notes='cd ~/personal-workspace/notes'
alias scripts='cd ~/personal-workspace/scripts'
""",

      "scripts/aliases/git_aliases": """# Git Aliases Configuration
# Git 命令别名配置

[alias]
  # 基础操作
  st = status
  co = checkout
  br = branch
  ci = commit
  di = diff
  
  # 日志查看
  lg = log --oneline --graph --decorate --all
  last = log -1 HEAD
  
  # 分支操作
  new = checkout -b
  del = branch -d
  
  # 暂存操作
  unstage = reset HEAD --
  
  # 远程操作
  sync = !git fetch && git rebase origin/main
  
  # 统计信息
  stats = shortlog -sn
  
  # 撤销操作
  undo = reset --soft HEAD~1
  
  # 清理操作
  cleanup = !git branch --merged | grep -v '\\*\\|main\\|master' | xargs -n 1 git branch -d
""",

      "scripts/aliases/custom_commands": """#!/bin/bash
# Custom Commands
# 自定义命令集合

# 快速导航到工作空间
workspace() {
  cd ~/personal-workspace
  echo "📂 已切换到个人工作空间"
  ls -la
}

# 创建新的笔记文件
newnote() {
  if [ -z "$1" ]; then
      echo "使用方法: newnote <文件名>"
      return 1
  fi
  
  local note_file="~/personal-workspace/notes/personal/daily/$(date +%Y-%m-%d)-$1.md"
  echo "# $1" > "$note_file"
  echo "" >> "$note_file"
  echo "创建日期: $(date)" >> "$note_file"
  echo "" >> "$note_file"
  echo "## 内容" >> "$note_file"
  echo "" >> "$note_file"
  
  echo "✅ 笔记文件已创建: $note_file"
}

# 快速备份重要文件
backup() {
  local backup_dir="~/personal-workspace/archive/backup-$(date +%Y%m%d)"
  mkdir -p "$backup_dir"
  
  if [ -z "$1" ]; then
      echo "使用方法: backup <文件或目录路径>"
      return 1
  fi
  
  cp -r "$1" "$backup_dir/"
  echo "✅ 文件已备份到: $backup_dir"
}

# 搜索笔记内容
searchnotes() {
  if [ -z "$1" ]; then
      echo "使用方法: searchnotes <搜索关键词>"
      return 1
  fi
  
  echo "🔍 在笔记中搜索: $1"
  grep -r "$1" ~/personal-workspace/notes/ --include="*.md"
}
"""
  }
  
  created_count = 0
  skipped_count = 0
  
  for file_path, content in templates.items():
      path = Path(file_path)
      
      if path.exists():
          print(f"⏭️  跳过已存在的文件: {file_path}")
          skipped_count += 1
      else:
          try:
              # 确保父目录存在
              path.parent.mkdir(parents=True, exist_ok=True)
              
              # 写入文件内容，替换日期占位符
              formatted_content = content.format(date=datetime.now().strftime("%Y-%m-%d"))
              
              with open(path, 'w', encoding='utf-8') as f:
                  f.write(formatted_content)
              
              print(f"✅ 创建文件: {file_path}")
              created_count += 1
              
          except Exception as e:
              print(f"❌ 创建文件失败 {file_path}: {e}")
  
  print("=" * 50)
  print(f"🎉 模板文件创建完成!")
  print(f"📊 统计信息:")
  print(f"   - 新创建: {created_count} 个文件")
  print(f"   - 已跳过: {skipped_count} 个文件")
  print(f"   - 总计: {len(templates)} 个文件")

if __name__ == "__main__":
  try:
      create_template_files()
  except KeyboardInterrupt:
      print("\n\n⚠️  操作被用户中断")
  except Exception as e:
      print(f"\n❌ 发生错误: {e}")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration Files Creator
创建配置文件的脚本
"""

import os
from pathlib import Path
from datetime import datetime

def create_config_files():
  """创建各种配置文件"""
  
  print("⚙️ 开始创建配置文件...")
  print("=" * 50)
  
  # 配置文件内容定义
  config_files = {
      # CHANGELOG.md
      "CHANGELOG.md": """# 更新日志

所有重要的项目更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 新增
- 初始化个人工作空间项目
- 创建完整的目录结构
- 添加文档和代码模板
- 配置 Git 别名和 Bash 别名

### 变更
- 无

### 修复
- 无

## [1.0.0] - {date}

### 新增
- 📁 创建完整的目录结构
- 📝 添加各种文档模板
- 🛠️ 创建实用脚本集合
- ⚙️ 配置开发环境模板
- 📖 生成详细的 README 文档
- 🏷️ 建立标签索引系统
- 🔍 提供搜索指南

### 项目里程碑
- ✅ 基础架构搭建完成
- ✅ 核心功能模块就绪
- ✅ 文档体系建立完善
- ✅ 自动化脚本部署完成

---

## 版本说明

### 版本格式
- **主版本号**: 不兼容的 API 修改
- **次版本号**: 向下兼容的功能性新增
- **修订号**: 向下兼容的问题修正

### 更新类型
- **新增**: 新功能
- **变更**: 对现有功能的变更
- **弃用**: 不久将移除的功能
- **移除**: 已移除的功能
- **修复**: 任何 bug 修复
- **安全**: 涉及安全的修复
""",

      # TAGS.md
      "TAGS.md": """# 🏷️ 标签索引系统

本文档提供了工作空间中使用的标签系统，帮助快速分类和查找内容。

## 📋 标签分类

### 🎯 内容类型标签

| 标签 | 描述 | 使用场景 |
|------|------|----------|
| `#tech` | 技术相关内容 | 编程、工具、框架学习 |
| `#learning` | 学习资料 | 课程笔记、教程、研究 |
| `#work` | 工作相关 | 项目、会议、任务 |
| `#personal` | 个人内容 | 日记、目标、反思 |
| `#gaming` | 游戏相关 | 攻略、评测、配置 |
| `#tools` | 工具和脚本 | 自动化、实用工具 |
| `#config` | 配置文件 | 环境配置、设置文件 |
| `#template` | 模板文件 | 文档模板、代码模板 |

### 🔧 技术栈标签

| 标签 | 描述 | 相关目录 |
|------|------|----------|
| `#python` | Python 相关 | `notes/tech/programming/` |
| `#javascript` | JavaScript 相关 | `notes/tech/programming/` |
| `#docker` | Docker 相关 | `configs/`, `scripts/` |
| `#git` | Git 相关 | `configs/development/git/` |
| `#vscode` | VS Code 相关 | `configs/development/vscode/` |
| `#linux` | Linux 相关 | `scripts/`, `configs/system/` |
| `#web` | Web 开发相关 | `notes/tech/frameworks/` |
| `#database` | 数据库相关 | `notes/tech/`, `scripts/` |

### 📊 优先级标签

| 标签 | 描述 | 使用建议 |
|------|------|----------|
| `#urgent` | 紧急重要 | 需要立即处理的内容 |
| `#important` | 重要但不紧急 | 重要的长期项目 |
| `#reference` | 参考资料 | 经常查阅的资料 |
| `#archive` | 归档内容 | 历史资料，不常用 |
| `#todo` | 待办事项 | 需要完成的任务 |
| `#done` | 已完成 | 已完成的任务或项目 |

## 🔍 标签使用指南

### 在文件中使用标签

#### Markdown 文件中
```markdown
# 文件标题

标签: #tech #python #learning #important

## 内容
...
```

### 搜索标签
```bash
# 搜索特定标签
grep -r "#tech" . --include="*.md"

# 搜索多个标签
grep -r "#tech.*#python" . --include="*.md"
```

## 🔄 标签更新日志

### {date}
- 创建初始标签系统
- 定义主要标签分类
- 建立使用规范
""",

      # SEARCH.md
      "SEARCH.md": """# 🔍 搜索指南

本指南提供了在个人工作空间中高效搜索和查找内容的方法。

## 🎯 搜索策略

### 1. 按内容搜索

#### 全文搜索
```bash
# 在所有 Markdown 文件中搜索关键词
grep -r "关键词" . --include="*.md"

# 忽略大小写搜索
grep -ri "关键词" . --include="*.md"

# 搜索多个关键词
grep -r "关键词1.*关键词2" . --include="*.md"
```

#### 精确搜索
```bash
# 搜索完整短语
grep -r "\"完整短语\"" . --include="*.md"

# 搜索以特定词开头的行
grep -r "^关键词" . --include="*.md"

# 搜索以特定词结尾的行
grep -r "关键词$" . --include="*.md"
```

### 2. 按标签搜索

#### 单个标签
```bash
# 搜索技术相关内容
grep -r "#tech" . --include="*.md"

# 搜索学习资料
grep -r "#learning" . --include="*.md"
```

#### 多个标签组合
```bash
# 搜索同时包含多个标签的文件
grep -r "#tech" . --include="*.md" | grep "#python"

# 搜索技术和学习相关的内容
grep -r "#tech.*#learning\|#learning.*#tech" . --include="*.md"
```

### 3. 按文件名搜索

#### 基础文件名搜索
```bash
# 查找包含特定词的文件
find . -name "*关键词*" -type f

# 查找特定扩展名的文件
find . -name "*.md" -type f
find . -name "*.py" -type f
find . -name "*.json" -type f
```

#### 高级文件名搜索
```bash
# 查找最近修改的文件
find . -name "*.md" -mtime -7 -type f

# 查找特定大小的文件
find . -name "*.md" -size +1k -type f

# 按日期范围查找文件
find . -name "2024-*" -type f
```

### 4. 按目录搜索

#### 特定目录搜索
```bash
# 在笔记目录中搜索
grep -r "关键词" ./notes/ --include="*.md"

# 在脚本目录中搜索
grep -r "关键词" ./scripts/ --include="*.py"

# 在配置目录中搜索
grep -r "关键词" ./configs/ --include="*.json" --include="*.yml"
```

#### 排除特定目录
```bash
# 排除归档目录的搜索
grep -r "关键词" . --include="*.md" --exclude-dir=archive

# 排除多个目录
grep -r "关键词" . --include="*.md" --exclude-dir={archive,temp,.git}
```

## 🛠️ 搜索工具

### 1. 命令行工具

#### grep 高级用法
```bash
# 显示匹配行的上下文
grep -r -A 3 -B 3 "关键词" . --include="*.md"

# 只显示匹配的文件名
grep -rl "关键词" . --include="*.md"

# 统计匹配次数
grep -rc "关键词" . --include="*.md"

# 高亮显示匹配内容
grep -r --color=always "关键词" . --include="*.md"
```

#### find 高级用法
```bash
# 查找并执行命令
find . -name "*.md" -exec grep -l "关键词" {} \;

# 查找空文件
find . -name "*.md" -empty -type f

# 查找大文件
find . -name "*.md" -size +100k -type f
```

### 2. 文本编辑器搜索

#### VS Code 搜索
- `Ctrl+Shift+F`: 全局搜索
- `Ctrl+Shift+H`: 全局替换
- 使用正则表达式搜索
- 按文件类型过滤

#### Vim 搜索
```vim
" 在当前文件中搜索
/关键词

" 在多个文件中搜索
:vimgrep /关键词/ **/*.md

" 替换
:%s/旧词/新词/g
```

## 📋 搜索模式

### 1. 日期相关搜索

#### 查找特定日期的内容
```bash
# 查找今天的笔记
find . -name "$(date +%Y-%m-%d)*" -type f

# 查找本周的内容
find . -name "$(date +%Y-%m)*" -type f

# 查找特定月份的内容
find . -name "2024-01*" -type f
```

#### 按时间范围搜索
```bash
# 查找最近 7 天修改的文件
find . -name "*.md" -mtime -7 -type f

# 查找超过 30 天未修改的文件
find . -name "*.md" -mtime +30 -type f
```

### 2. 项目相关搜索

#### 搜索待办事项
```bash
# 查找所有 TODO 项
grep -r "TODO\|todo\|待办" . --include="*.md"

# 查找已完成项
grep -r "DONE\|done\|已完成" . --include="*.md"

# 查找重要标记
grep -r "IMPORTANT\|important\|重要" . --include="*.md"
```

#### 搜索代码相关
```bash
# 查找代码块
grep -r "```" . --include="*.md"

# 查找特定编程语言
grep -r "```python\|```javascript\|```bash" . --include="*.md"
```

### 3. 配置相关搜索

#### 搜索配置文件
```bash
# 查找所有配置文件
find . -name "*.json" -o -name "*.yml" -o -name "*.yaml" -o -name "*.conf"

# 搜索特定配置项
grep -r "port\|host\|password" ./configs/ --include="*.json" --include="*.yml"
```

## 🎨 搜索结果处理

### 1. 结果过滤

#### 按文件类型过滤
```bash
# 只搜索 Markdown 文件
grep -r "关键词" . --include="*.md"

# 排除特定文件类型
grep -r "关键词" . --exclude="*.log" --exclude="*.tmp"
```

#### 按内容过滤
```bash
# 搜索包含特定标签的文件
grep -r "#tech" . --include="*.md" | grep -v "#archive"

# 搜索不包含特定词的文件
grep -r "关键词" . --include="*.md" | grep -v "排除词"
```

### 2. 结果排序

#### 按时间排序
```bash
# 按修改时间排序
find . -name "*.md" -printf "%T@ %p\n" | sort -n | cut -d' ' -f2-

# 按创建时间排序
ls -lt $(find . -name "*.md")
```

#### 按大小排序
```bash
# 按文件大小排序
find . -name "*.md" -printf "%s %p\n" | sort -n
```

## 🚀 高效搜索技巧

### 1. 创建搜索别名
```bash
# 添加到 ~/.bashrc 或 ~/.zshrc
alias searchnotes='grep -r --include="*.md"'
alias findnotes='find . -name "*.md" -type f'
alias searchcode='grep -r --include="*.py" --include="*.js" --include="*.sh"'
```

### 2. 使用搜索脚本
```bash
#!/bin/bash
# 快速搜索脚本
search_workspace() {
  if [ -z "$1" ]; then
      echo "使用方法: search_workspace <关键词>"
      return 1
  fi
  
  echo "🔍 搜索关键词: $1"
  echo "=" * 50
  
  echo "📝 在笔记中搜索:"
  grep -r "$1" ./notes/ --include="*.md" | head -10
  
  echo -e "\n🛠️ 在脚本中搜索:"
  grep -r "$1" ./scripts/ --include="*.py" --include="*.sh" | head -5
  
  echo -e "\n⚙️ 在配置中搜索:"
  grep -r "$1" ./configs/ --include="*.json" --include="*.yml" | head -5
}
```

### 3. 正则表达式搜索
```bash
# 搜索邮箱地址
grep -r "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" . --include="*.md"

# 搜索 URL
grep -r "https\?://[^\s]+" . --include="*.md"

# 搜索日期格式
grep -r "[0-9]{4}-[0-9]{2}-[0-9]{2}" . --include="*.md"
```

## 📊 搜索性能优化

### 1. 索引建立
```bash
# 使用 locate 建立文件索引
sudo updatedb

# 快速查找文件
locate personal-workspace
```

### 2. 缓存搜索结果
```bash
# 将常用搜索结果保存到文件
grep -r "#tech" . --include="*.md" > tech_files.txt
grep -r "#learning" . --include="*.md" > learning_files.txt
```

---

*最后更新: {date}*

**💡 提示**: 定期更新搜索索引和清理临时文件可以提高搜索效率。
""",

      # .gitignore
      ".gitignore": """# 个人工作空间 .gitignore

# 系统文件
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# 编辑器文件
.vscode/
.idea/
*.swp
*.swo
*~

# 临时文件
*.tmp
*.temp
*.log
*.cache

# 个人敏感信息
**/private/
**/secrets/
**/*secret*
**/*password*
**/*key*
*.pem
*.key

# 游戏存档（如果包含敏感信息）
gaming/saves/private/
gaming/saves/**/account/

# 大文件
*.iso
*.dmg
*.zip
*.rar
*.tar.gz

# 编译文件
*.pyc
__pycache__/
*.class
*.o
*.so

# 依赖目录
node_modules/
venv/
env/

# 备份文件
*.bak
*.backup
*~

# 操作系统
# Windows
desktop.ini

# Linux
*~

# macOS
.AppleDouble
.LSOverride

# 特定目录
temp/
tmp/
cache/
logs/
""",

      # LICENSE
      "LICENSE": """MIT License

Copyright (c) {year} Personal Workspace

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",

      # 资源文件
      "resources/bookmarks/development.md": """# 开发相关书签

标签: #bookmarks #development #resources

## 📚 学习资源

### 在线教程
- [MDN Web Docs](https://developer.mozilla.org/) - Web 开发权威文档
- [W3Schools](https://www.w3schools.com/) - Web 技术教程
- [freeCodeCamp](https://www.freecodecamp.org/) - 免费编程课程
- [Codecademy](https://www.codecademy.com/) - 交互式编程学习

### 技术博客
- [Stack Overflow](https://stackoverflow.com/) - 编程问答社区
- [GitHub](https://github.com/) - 代码托管平台
- [Dev.to](https://dev.to/) - 开发者社区
- [Medium](https://medium.com/) - 技术文章平台

## 🛠️ 开发工具

### 代码编辑器
- [Visual Studio Code](https://code.visualstudio.com/) - 免费代码编辑器
- [Sublime Text](https://www.sublimetext.com/) - 轻量级编辑器
- [Atom](https://atom.io/) - GitHub 开发的编辑器

### 版本控制
- [Git](https://git-scm.com/) - 版本控制系统
- [GitHub Desktop](https://desktop.github.com/) - Git 图形界面
- [GitLab](https://gitlab.com/) - Git 代码托管

### API 工具
- [Postman](https://www.postman.com/) - API 测试工具
- [Insomnia](https://insomnia.rest/) - REST 客户端
- [Swagger](https://swagger.io/) - API 文档工具

## 🎨 设计资源

### UI/UX 设计
- [Figma](https://www.figma.com/) - 界面设计工具
- [Adobe XD](https://www.adobe.com/products/xd.html) - 原型设计
- [Sketch](https://www.sketch.com/) - macOS 设计工具

### 图标和图片
- [Font Awesome](https://fontawesome.com/) - 图标库
- [Unsplash](https://unsplash.com/) - 免费高质量图片
- [Pixabay](https://pixabay.com/) - 免费图片资源

## 🚀 部署和托管

### 云服务
- [AWS](https://aws.amazon.com/) - 亚马逊云服务
- [Google Cloud](https://cloud.google.com/) - 谷歌云平台
- [Microsoft Azure](https://azure.microsoft.com/) - 微软云服务

### 静态网站托管
- [Netlify](https://www.netlify.com/) - 静态网站托管
- [Vercel](https://vercel.com/) - 前端部署平台
- [GitHub Pages](https://pages.github.com/) - 免费静态托管

---

*最后更新: {date}*
""",

      "resources/bookmarks/learning.md": """# 学习资源书签

标签: #bookmarks #learning #education

## 📚 在线课程平台

### 综合性平台
- [Coursera](https://www.coursera.org/) - 大学课程和专业证书
- [edX](https://www.edx.org/) - 哈佛、MIT 等名校课程
- [Udemy](https://www.udemy.com/) - 实用技能课程
- [Khan Academy](https://www.khanacademy.org/) - 免费教育资源

### 技术专业平台
- [Pluralsight](https://www.pluralsight.com/) - 技术技能培训
- [LinkedIn Learning](https://www.linkedin.com/learning/) - 职业技能课程
- [Skillshare](https://www.skillshare.com/) - 创意技能学习

## 🎓 学术资源

### 论文和期刊
- [Google Scholar](https://scholar.google.com/) - 学术搜索引擎
- [arXiv](https://arxiv.org/) - 预印本论文库
- [ResearchGate](https://www.researchgate.net/) - 学术社交网络
- [JSTOR](https://www.jstor.org/) - 学术期刊数据库

### 开放课程
- [MIT OpenCourseWare](https://ocw.mit.edu/) - MIT 开放课程
- [Stanford Online](https://online.stanford.edu/) - 斯坦福在线课程
- [Harvard Online Learning](https://online-learning.harvard.edu/) - 哈佛在线学习

## 📖 电子书和文档

### 免费电子书
- [Project Gutenberg](https://www.gutenberg.org/) - 免费经典文学
- [Open Library](https://openlibrary.org/) - 开放图书馆
- [Bookboon](https://bookboon.com/) - 免费教科书

### 技术文档
- [Read the Docs](https://readthedocs.org/) - 技术文档托管
- [GitBook](https://www.gitbook.com/) - 文档和知识管理
- [Notion](https://www.notion.so/) - 笔记和知识管理

## 🧠 学习方法

### 记忆和复习
- [Anki](https://apps.ankiweb.net/) - 间隔重复记忆卡片
- [Quizlet](https://quizlet.com/) - 学习卡片和测验
- [Memrise](https://www.memrise.com/) - 语言学习平台

### 专注和效率
- [Pomodoro Timer](https://pomofocus.io/) - 番茄工作法计时器
- [Forest](https://www.forestapp.cc/) - 专注力培养应用
- [RescueTime](https://www.rescuetime.com/) - 时间跟踪工具

---

*最后更新: {date}*
""",

      "resources/bookmarks/tools.md": """# 工具资源书签

标签: #bookmarks #tools #productivity

## 💻 生产力工具

### 笔记和文档
- [Notion](https://www.notion.so/) - 全能笔记和项目管理
- [Obsidian](https://obsidian.md/) - 知识图谱笔记
- [Roam Research](https://roamresearch.com/) - 网络化思维笔记
- [Typora](https://typora.io/) - Markdown 编辑器

### 项目管理
- [Trello](https://trello.com/) - 看板式项目管理
- [Asana](https://asana.com/) - 团队协作工具
- [Monday.com](https://monday.com/) - 工作管理平台
- [Jira](https://www.atlassian.com/software/jira) - 敏捷项目管理

### 时间管理
- [Toggl](https://toggl.com/) - 时间跟踪工具
- [Clockify](https://clockify.me/) - 免费时间跟踪
- [RescueTime](https://www.rescuetime.com/) - 自动时间跟踪

## 🛠️ 开发工具

### 代码质量
- [SonarQube](https://www.sonarqube.org/) - 代码质量检测
- [ESLint](https://eslint.org/) - JavaScript 代码检查
- [Prettier](https://prettier.io/) - 代码格式化工具

### 数据库工具
- [phpMyAdmin](https://www.phpmyadmin.net/) - MySQL 管理工具
- [MongoDB Compass](https://www.mongodb.com/products/compass) - MongoDB GUI
- [DBeaver](https://dbeaver.io/) - 通用数据库工具

### 网络工具
- [Wireshark](https://www.wireshark.org/) - 网络协议分析
- [Nmap](https://nmap.org/) - 网络扫描工具
- [Ping](https://www.ping.eu/) - 在线网络测试

## 🎨 设计工具

### 图像编辑
- [GIMP](https://www.gimp.org/) - 免费图像编辑
- [Canva](https://www.canva.com/) - 在线设计工具
- [Figma](https://www.figma.com/) - 界面设计工具

### 图标和素材
- [Flaticon](https://www.flaticon.com/) - 免费图标库
- [Iconfinder](https://www.iconfinder.com/) - 图标搜索引擎
- [Pexels](https://www.pexels.com/) - 免费股票照片

## 🔧 系统工具

### 系统监控
- [htop](https://htop.dev/) - 系统进程监控
- [Glances](https://nicolargo.github.io/glances/) - 系统监控工具
- [Netdata](https://www.netdata.cloud/) - 实时性能监控

### 文件管理
- [7-Zip](https://www.7-zip.org/) - 文件压缩工具
- [WinDirStat](https://windirstat.net/) - 磁盘使用分析
- [Everything](https://www.voidtools.com/) - 文件搜索工具

---

*最后更新: {date}*
"""
  }
  
  created_count = 0
  skipped_count = 0
  
  for file_path, content in config_files.items():
      path = Path(file_path)
      
      if path.exists():
          print(f"⏭️  跳过已存在的文件: {file_path}")
          skipped_count += 1
      else:
          try:
              # 确保父目录存在
              path.parent.mkdir(parents=True, exist_ok=True)
              
              # 写入文件内容，替换日期占位符
              formatted_content = content.format(
                  date=datetime.now().strftime("%Y-%m-%d"),
                  year=datetime.now().year
              )
              
              with open(path, 'w', encoding='utf-8') as f:
                  f.write(formatted_content)
              
              print(f"✅ 创建文件: {file_path}")
              created_count += 1
              
          except Exception as e:
              print(f"❌ 创建文件失败 {file_path}: {e}")
  
  print("=" * 50)
  print(f"🎉 配置文件创建完成!")
  print(f"📊 统计信息:")
  print(f"   - 新创建: {created_count} 个文件")
  print(f"   - 已跳过: {skipped_count} 个文件")
  print(f"   - 总计: {len(config_files)} 个文件")

if __name__ == "__main__":
  try:
      create_config_files()
  except KeyboardInterrupt:
      print("\n\n⚠️  操作被用户中断")
  except Exception as e:
      print(f"\n❌ 发生错误: {e}")
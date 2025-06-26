#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated README Generator with Optimized Navigation
生成带有优化导航的 README 文件 - 替换原 create_readme.py
"""

import os
from pathlib import Path
from datetime import datetime

def create_optimized_readme():
  """创建优化版 README.md 文件"""
  
  print("📖 开始生成优化版 README.md 文件...")
  print("=" * 50)
  
  readme_content = f"""# 🗂️ Personal Workspace

> 个人数字工作空间 - 统一管理知识、工具和资源的集成化仓库

[![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/personal-workspace)]()
[![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/personal-workspace)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

## 📋 目录

- [🎯 项目简介](#-项目简介)
- [📁 目录结构](#-目录结构)
- [🗂️ 快速导航](#️-快速导航)
- [🚀 快速开始](#-快速开始)
- [📚 使用指南](#-使用指南)
- [🔧 配置说明](#-配置说明)
- [📖 文档索引](#-文档索引)
- [🏷️ 标签系统](#️-标签系统)
- [🤝 贡献指南](#-贡献指南)

## 🎯 项目简介

这是一个个人数字工作空间，用于统一管理和组织：

- 📚 **学习笔记** - 技术学习、课程笔记、读书心得
- 🛠️ **实用脚本** - 自动化脚本、安装脚本、工具集合
- 🎨 **图表设计** - 架构图、流程图、思维导图
- 🎮 **游戏资源** - 游戏攻略、配置文件、评测记录
- ⚙️ **配置模板** - 开发环境、系统配置、应用设置
- 📋 **项目模板** - 文档模板、代码模板、工作流模板

## 📁 目录结构

### 整体结构概览

```
personal-workspace/
├── 📚 notes/                          # 笔记文档
│   ├── 💻 tech/                       # 技术相关笔记
│   ├── 📖 learning/                   # 学习相关笔记
│   ├── 💼 work/                       # 工作相关笔记
│   └── 👤 personal/                   # 个人笔记
├── 🛠️ scripts/                        # 脚本工具
│   ├── 📦 install/                    # 安装脚本
│   ├── 🤖 automation/                 # 自动化脚本
│   ├── 🔧 utilities/                  # 实用工具
│   └── 🏷️ aliases/                    # 命令别名
├── 🎨 diagrams/                       # 图表设计
├── 🎮 gaming/                         # 游戏资源
├── ⚙️ configs/                        # 配置文件
├── 📋 templates/                      # 模板文件
├── 🔗 resources/                      # 资源链接
├── 📊 tracking/                       # 进度追踪
└── 🗄️ archive/                        # 归档文件
```

## 🗂️ 快速导航

### 📚 笔记文档
| 分类 | 描述 | 快速链接 |
|------|------|----------|
| 💻 技术笔记 | 编程、工具、框架学习 | [📂 tech](./notes/tech/) \| [🐍 programming](./notes/tech/programming/) \| [🔧 tools](./notes/tech/tools/) \| [🏗️ frameworks](./notes/tech/frameworks/) |
| 📖 学习笔记 | 课程、书籍、教程记录 | [📂 learning](./notes/learning/) \| [🎓 courses](./notes/learning/courses/) \| [📚 books](./notes/learning/books/) \| [📝 tutorials](./notes/learning/tutorials/) |
| 💼 工作笔记 | 项目、会议、想法记录 | [📂 work](./notes/work/) \| [🚀 projects](./notes/work/projects/) \| [🤝 meetings](./notes/work/meetings/) \| [💡 ideas](./notes/work/ideas/) |
| 👤 个人笔记 | 日常、目标、反思总结 | [📂 personal](./notes/personal/) \| [📅 daily](./notes/personal/daily/) \| [🎯 goals](./notes/personal/goals/) \| [🤔 reflections](./notes/personal/reflections/) |

### 🛠️ 脚本工具
| 分类 | 描述 | 快速链接 |
|------|------|----------|
| 📦 安装脚本 | 开发环境和应用安装 | [📂 install](./scripts/install/) \| [💻 dev-environment](./scripts/install/dev-environment/) \| [📱 applications](./scripts/install/applications/) |
| 🤖 自动化脚本 | 备份、部署、监控维护 | [📂 automation](./scripts/automation/) \| [💾 backup](./scripts/automation/backup/) \| [🚀 deployment](./scripts/automation/deployment/) |
| 🔧 实用工具 | 文件管理和数据处理 | [📂 utilities](./scripts/utilities/) \| [📁 file-management](./scripts/utilities/file-management/) \| [📊 data-processing](./scripts/utilities/data-processing/) |
| 🏷️ 命令别名 | Bash、Git、自定义命令 | [📂 aliases](./scripts/aliases/) \| [⚡ bash_aliases](./scripts/aliases/bash_aliases) \| [🔀 git_aliases](./scripts/aliases/git_aliases) |

### 🎨 设计资源
| 分类 | 描述 | 快速链接 |
|------|------|----------|
| 🖼️ Draw.io 图表 | 架构图、流程图、网络图 | [📂 drawio](./diagrams/drawio/) \| [🏗️ architecture](./diagrams/drawio/architecture/) \| [📊 flowcharts](./diagrams/drawio/flowcharts/) |
| 🧠 思维导图 | 学习、项目、头脑风暴 | [📂 mindmaps](./diagrams/mindmaps/) \| [📚 learning](./diagrams/mindmaps/learning/) \| [🚀 projects](./diagrams/mindmaps/projects/) |
| 📊 PlantUML | UML 图表和文档 | [📂 plantuml](./diagrams/plantuml/) \| [🖼️ exports](./diagrams/exports/) |

### 🎮 游戏资源
| 分类 | 描述 | 快速链接 |
|------|------|----------|
| 📖 游戏指南 | 攻略、策略、技巧分享 | [📂 guides](./gaming/guides/) \| [🗺️ walkthroughs](./gaming/guides/walkthroughs/) \| [🎯 strategies](./gaming/guides/strategies/) |
| ⚙️ 游戏配置 | 设置、MOD、按键绑定 | [📂 configs](./gaming/configs/) \| [🎮 game-settings](./gaming/configs/game-settings/) \| [⌨️ keybindings](./gaming/configs/keybindings/) |
| 📝 游戏评测 | 游戏评测、硬件推荐 | [📂 reviews](./gaming/reviews/) \| [🎮 game-reviews](./gaming/reviews/game-reviews/) \| [🔧 hardware-reviews](./gaming/reviews/hardware-reviews/) |

### ⚙️ 配置文件
| 分类 | 描述 | 快速链接 |
|------|------|----------|
| 💻 开发配置 | VS Code、Git、终端配置 | [📂 development](./configs/development/) \| [🆚 vscode](./configs/development/vscode/) \| [🔀 git](./configs/development/git/) |
| 🖥️ 系统配置 | 系统文件、环境变量 | [📂 system](./configs/system/) \| [⚙️ dotfiles](./configs/system/dotfiles/) \| [🌍 environment](./configs/system/environment/) |
| 📱 应用配置 | 浏览器、媒体、生产力工具 | [📂 applications](./configs/applications/) \| [🌐 browsers](./configs/applications/browsers/) \| [🎵 media](./configs/applications/media/) |

### 📋 模板文件
| 分类 | 描述 | 快速链接 |
|------|------|----------|
| 📄 文档模板 | 会议记录、项目计划模板 | [📂 documents](./templates/documents/) \| [📝 meeting-notes.md](./templates/documents/meeting-notes.md) \| [📊 project-plan.md](./templates/documents/project-plan.md) |
| 💻 代码模板 | 项目结构、代码片段 | [📂 code](./templates/code/) \| [🏗️ project-structure](./templates/code/project-structure/) \| [📖 readme-template.md](./templates/code/readme-template.md) |
| ⚙️ 配置模板 | Docker、CI/CD、部署模板 | [📂 configs](./templates/configs/) \| [🐳 docker](./templates/configs/docker/) \| [🔄 ci-cd](./templates/configs/ci-cd/) |

### 🔗 资源链接
| 分类 | 描述 | 快速链接 |
|------|------|----------|
| 🔖 书签收藏 | 开发、学习、工具资源 | [📂 bookmarks](./resources/bookmarks/) \| [💻 development.md](./resources/bookmarks/development.md) \| [📚 learning.md](./resources/bookmarks/learning.md) |
| 📋 速查表 | 常用命令和语法参考 | [📂 cheatsheets](./resources/cheatsheets/) \| [📚 references](./resources/references/) \| [📥 downloads](./resources/downloads/) |

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/yourusername/personal-workspace.git
cd personal-workspace
```

### 2. 运行初始化脚本
```bash
# 一键设置（推荐）
python3 setup.py

# 或分步执行(scripts\utilities\file-management\dirgen)
python3 create_directories.py      # 创建目录结构
python3 create_template_files.py   # 创建模板文件
python3 create_readme.py           # 生成 README 文件
python3 create_config_files.py     # 创建配置文件
python3 create_dev_configs.py      # 创建开发环境配置
```

### 3. 配置个人信息
```bash
# 编辑 Git 配置
nano configs/development/git/gitconfig

# 设置命令别名
source scripts/aliases/bash_aliases
```

## 📚 使用指南

### 📝 笔记管理
- **格式**: 使用 Markdown 格式编写笔记
- **组织**: 按照主题和日期组织文件
- **标签**: 使用标签进行分类管理
- **链接**: 利用内部链接建立知识网络

### 🛠️ 脚本使用
- **文档**: 所有脚本都有详细的使用说明
- **安全**: 运行前请仔细阅读脚本注释
- **测试**: 建议先在测试环境中验证

### 🎨 图表制作
- **Draw.io**: 统一存放在 `diagrams/drawio/` 目录
- **导出**: 图片保存在 `diagrams/exports/` 目录
- **思维导图**: 使用 `.xmind` 或 `.mm` 格式

## 🔧 配置说明

### 环境变量
在 `configs/system/environment/` 目录下配置：
- [`dev.env`](./configs/system/environment/dev.env) - 开发环境变量
- [`prod.env`](./configs/system/environment/prod.env) - 生产环境变量

### 开发工具配置
- **VS Code**: 配置文件在 [`configs/development/vscode/`](./configs/development/vscode/)
- **Git**: 全局配置在 [`configs/development/git/`](./configs/development/git/)
- **Terminal**: 终端配置在 [`configs/development/terminal/`](./configs/development/terminal/)

## 📖 文档索引

### 📚 重要文档
- [📋 更新日志](./CHANGELOG.md) - 记录重要更新和变更
- [🏷️ 标签索引](./TAGS.md) - 快速查找文件的标签系统
- [🔍 搜索指南](./SEARCH.md) - 高效搜索和查找技巧

### 📋 模板文档
- [📝 会议记录模板](./templates/documents/meeting-notes.md)
- [📊 项目计划模板](./templates/documents/project-plan.md)
- [🗣️ 日常站会模板](./templates/documents/daily-standup.md)
- [🔄 回顾总结模板](./templates/documents/retrospective.md)

## 🏷️ 标签系统

使用标签快速分类和查找内容：

| 标签类型 | 标签示例 | 使用场景 |
|----------|----------|----------|
| 📋 内容类型 | `#tech` `#learning` `#work` `#personal` | 按内容性质分类 |
| 🔧 技术栈 | `#python` `#javascript` `#docker` `#git` | 按技术类型分类 |
| 📊 优先级 | `#urgent` `#important` `#reference` `#todo` | 按重要程度分类 |
| 🎮 游戏类型 | `#strategy` `#rpg` `#fps` `#indie` | 按游戏类型分类 |

详细标签使用指南请查看 [🏷️ 标签索引](./TAGS.md)

## 🔍 搜索技巧

### 全局搜索
```bash
# 搜索所有 Markdown 文件
grep -r "关键词" . --include="*.md"

# 搜索特定目录
grep -r "关键词" ./notes/ --include="*.md"

# 使用标签搜索
grep -r "#tech" . --include="*.md"
```

### 文件名搜索
```bash
# 查找特定文件
find . -name "*关键词*" -type f

# 查找特定类型文件
find . -name "*.md" -type f
```

完整搜索指南请查看 [🔍 搜索指南](./SEARCH.md)

## 📊 统计信息

*最后更新: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*

- 📁 总目录数: 60+
- 📄 模板文件: 15+
- 🛠️ 脚本工具: 6+
- 📚 文档类型: Markdown, Draw.io, PlantUML
- 🔗 快速链接: 100+

## 🤝 贡献指南

### 添加新内容
1. 按照现有目录结构组织文件
2. 使用统一的命名规范
3. 添加适当的标签和说明
4. 更新相关的索引文件

### 文件命名规范
- 使用小写字母和连字符
- 包含日期的文件格式: `YYYY-MM-DD-filename`
- 避免使用特殊字符和空格

### 提交规范
```bash
# 提交格式
git commit -m "类型(范围): 描述"

# 示例
git commit -m "docs(notes): 添加 Python 学习笔记"
git commit -m "feat(scripts): 新增自动备份脚本"
git commit -m "fix(config): 修复 VS Code 配置问题"
```

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)

## 🙏 致谢

感谢所有为个人知识管理和效率提升做出贡献的工具和社区！

---

**💡 提示**: 这是一个活跃维护的个人工作空间，内容会持续更新和完善。

**🔗 导航提示**: 点击表格中的链接可以快速跳转到对应目录，代码块中的路径仅供参考。

*Happy Coding & Learning! 🚀*
"""
  
  try:
      with open("README.md", 'w', encoding='utf-8') as f:
          f.write(readme_content)
      
      print("✅ 优化版 README.md 文件创建成功!")
      print("📊 优化特性:")
      print("   - 🔗 表格形式的可点击链接导航")
      print("   - 📋 保留代码块的树状结构展示")
      print("   - 🎯 快速导航区域，按分类整理")
      print("   - 📱 移动端友好的表格布局")
      print("   - 🏷️ 标签系统集成")
      
  except Exception as e:
      print(f"❌ 创建优化版 README.md 失败: {e}")

if __name__ == "__main__":
  try:
      create_optimized_readme()
  except KeyboardInterrupt:
      print("\n\n⚠️  操作被用户中断")
  except Exception as e:
      print(f"\n❌ 发生错误: {e}")
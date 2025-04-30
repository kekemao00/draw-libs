# 🗂️ Personal Workspace

> 个人数字工作空间 - 统一管理知识、工具和资源的集成化仓库

[![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/personal-workspace)]()
[![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/personal-workspace)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

## 📋 目录

- [🎯 项目简介](#-项目简介)
- [📁 目录结构](#-目录结构)
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

```
personal-workspace/
├── 📚 notes/                          # 笔记文档
│   ├── 💻 [tech/](./notes/tech/)                     # 技术相关笔记
│   │   ├── [programming/](./notes/tech/programming/)         # 编程笔记
│   │   ├── [tools/](./notes/tech/tools/)                   # 工具使用笔记
│   │   ├── [frameworks/](./notes/tech/frameworks/)           # 框架学习笔记
│   │   └── [troubleshooting/](./notes/tech/troubleshooting/) # 问题解决记录
│   ├── 📖 [learning/](./notes/learning/)             # 学习相关笔记
│   │   ├── [courses/](./notes/learning/courses/)           # 课程笔记
│   │   ├── [books/](./notes/learning/books/)               # 读书笔记
│   │   ├── [tutorials/](./notes/learning/tutorials/)       # 教程笔记
│   │   └── [research/](./notes/learning/research/)         # 研究资料
│   ├── 💼 [work/](./notes/work/)                     # 工作相关笔记
│   │   ├── [projects/](./notes/work/projects/)             # 项目相关
│   │   ├── [meetings/](./notes/work/meetings/)             # 会议记录
│   │   └── [ideas/](./notes/work/ideas/)                   # 想法记录
│   └── 👤 [personal/](./notes/personal/)             # 个人笔记
│       ├── [daily/](./notes/personal/daily/)               # 日常记录
│       ├── [goals/](./notes/personal/goals/)               # 目标规划
│       └── [reflections/](./notes/personal/reflections/)   # 反思总结
│
├── 🛠️ scripts/                        # 脚本工具
│   ├── 📦 [install/](./scripts/install/)             # 安装脚本
│   │   ├── [dev-environment/](./scripts/install/dev-environment/) # 开发环境安装
│   │   ├── [applications/](./scripts/install/applications/)       # 应用程序安装
│   │   └── [system-setup/](./scripts/install/system-setup/)       # 系统配置
│   ├── 🤖 [automation/](./scripts/automation/)       # 自动化脚本
│   │   ├── [backup/](./scripts/automation/backup/)             # 备份脚本
│   │   ├── [deployment/](./scripts/automation/deployment/)     # 部署脚本
│   │   ├── [monitoring/](./scripts/automation/monitoring/)     # 监控脚本
│   │   └── [maintenance/](./scripts/automation/maintenance/)   # 维护脚本
│   ├── 🔧 [utilities/](./scripts/utilities/)         # 实用工具
│   │   ├── [file-management/](./scripts/utilities/file-management/) # 文件管理
│   │   ├── [data-processing/](./scripts/utilities/data-processing/) # 数据处理
│   │   └── [system-tools/](./scripts/utilities/system-tools/)       # 系统工具
│   └── 🏷️ [aliases/](./scripts/aliases/)             # 命令别名
│       ├── [bash_aliases](./scripts/aliases/bash_aliases)      # Bash 别名
│       ├── [git_aliases](./scripts/aliases/git_aliases)        # Git 别名
│       └── [custom_commands](./scripts/aliases/custom_commands) # 自定义命令
│
├── 🎨 diagrams/                       # 图表设计
│   ├── 🖼️ [drawio/](./diagrams/drawio/)              # Draw.io 文件
│   │   ├── [architecture/](./diagrams/drawio/architecture/)   # 架构图
│   │   ├── [flowcharts/](./diagrams/drawio/flowcharts/)       # 流程图
│   │   ├── [network/](./diagrams/drawio/network/)             # 网络拓扑图
│   │   └── [ui-mockups/](./diagrams/drawio/ui-mockups/)       # UI 原型图
│   ├── 🧠 [mindmaps/](./diagrams/mindmaps/)          # 思维导图
│   │   ├── [learning/](./diagrams/mindmaps/learning/)         # 学习思维导图
│   │   ├── [projects/](./diagrams/mindmaps/projects/)         # 项目思维导图
│   │   └── [brainstorming/](./diagrams/mindmaps/brainstorming/) # 头脑风暴
│   ├── 📊 [plantuml/](./diagrams/plantuml/)          # PlantUML 图表
│   └── 🖼️ [exports/](./diagrams/exports/)            # 导出的图片文件
│
├── 🎮 gaming/                         # 游戏资源
│   ├── 📖 [guides/](./gaming/guides/)                # 游戏指南
│   │   ├── [walkthroughs/](./gaming/guides/walkthroughs/)     # 游戏攻略
│   │   ├── [strategies/](./gaming/guides/strategies/)         # 策略指南
│   │   └── [tips-tricks/](./gaming/guides/tips-tricks/)       # 技巧分享
│   ├── ⚙️ [configs/](./gaming/configs/)              # 游戏配置
│   │   ├── [game-settings/](./gaming/configs/game-settings/)  # 游戏设置
│   │   ├── [mods/](./gaming/configs/mods/)                    # MOD 配置
│   │   └── [keybindings/](./gaming/configs/keybindings/)      # 按键绑定
│   ├── 📝 [reviews/](./gaming/reviews/)              # 游戏评测
│   │   ├── [game-reviews/](./gaming/reviews/game-reviews/)    # 游戏评测
│   │   ├── [hardware-reviews/](./gaming/reviews/hardware-reviews/) # 硬件评测
│   │   └── [recommendations/](./gaming/reviews/recommendations/)    # 推荐列表
│   └── 💾 [saves/](./gaming/saves/)                  # 游戏存档备份
│
├── ⚙️ configs/                        # 配置文件
│   ├── 💻 [development/](./configs/development/)      # 开发配置
│   │   ├── [vscode/](./configs/development/vscode/)           # VS Code 配置
│   │   ├── [git/](./configs/development/git/)                 # Git 配置
│   │   ├── [terminal/](./configs/development/terminal/)       # 终端配置
│   │   └── [editors/](./configs/development/editors/)         # 编辑器配置
│   ├── 🖥️ [system/](./configs/system/)               # 系统配置
│   │   ├── [dotfiles/](./configs/system/dotfiles/)           # 系统配置文件
│   │   ├── [environment/](./configs/system/environment/)     # 环境变量
│   │   └── [startup/](./configs/system/startup/)             # 启动脚本
│   └── 📱 [applications/](./configs/applications/)   # 应用配置
│       ├── [browsers/](./configs/applications/browsers/)     # 浏览器配置
│       ├── [media/](./configs/applications/media/)           # 媒体软件配置
│       └── [productivity/](./configs/applications/productivity/) # 生产力工具配置
│
├── 📋 templates/                      # 模板文件
│   ├── 📄 [documents/](./templates/documents/)       # 文档模板
│   │   ├── [meeting-notes.md](./templates/documents/meeting-notes.md)     # 会议记录模板
│   │   ├── [project-plan.md](./templates/documents/project-plan.md)       # 项目计划模板
│   │   ├── [daily-standup.md](./templates/documents/daily-standup.md)     # 日常站会模板
│   │   └── [retrospective.md](./templates/documents/retrospective.md)     # 回顾总结模板
│   ├── 💻 [code/](./templates/code/)                 # 代码模板
│   │   ├── [project-structure/](./templates/code/project-structure/)     # 项目结构模板
│   │   ├── [readme-template.md](./templates/code/readme-template.md)     # README 模板
│   │   └── [code-snippets/](./templates/code/code-snippets/)             # 代码片段
│   └── ⚙️ [configs/](./templates/configs/)           # 配置模板
│       ├── [docker/](./templates/configs/docker/)           # Docker 模板
│       ├── [ci-cd/](./templates/configs/ci-cd/)             # CI/CD 模板
│       └── [deployment/](./templates/configs/deployment/)   # 部署模板
│
├── 🔗 resources/                      # 资源链接
│   ├── 🔖 [bookmarks/](./resources/bookmarks/)       # 书签收藏
│   ├── 📋 [cheatsheets/](./resources/cheatsheets/)   # 速查表
│   ├── 📚 [references/](./resources/references/)     # 参考资料
│   └── 📥 [downloads/](./resources/downloads/)       # 下载资源
│
├── 📊 tracking/                       # 进度追踪
│   ├── 📈 [habits/](./tracking/habits/)              # 习惯追踪
│   ├── 🎯 [goals/](./tracking/goals/)                # 目标进度
│   ├── 📖 [learning-progress/](./tracking/learning-progress/) # 学习进度
│   └── 📋 [project-status/](./tracking/project-status/)     # 项目状态
│
├── 🗄️ archive/                        # 归档文件
│   ├── 📁 [old-projects/](./archive/old-projects/)   # 旧项目归档
│   ├── 🗑️ [deprecated-scripts/](./archive/deprecated-scripts/) # 废弃脚本
│   └── 📜 [historical-notes/](./archive/historical-notes/)     # 历史笔记
│
├── 📖 [README.md](./README.md)                        # 项目说明文档
├── 📋 [CHANGELOG.md](./CHANGELOG.md)                  # 更新日志
├── 🏷️ [TAGS.md](./TAGS.md)                           # 标签索引
└── 🔍 [SEARCH.md](./SEARCH.md)                       # 搜索指南
```

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/kekemao00/personal-workspace.git
cd personal-workspace
```

### 2. 运行初始化脚本
```bash

# 创建目录结构
python3 create_directories.py

# 创建模板文件
python3 create_template_files.py

# 生成 README 文件
python3 create_readme.py

# 创建其他配置文件
python3 create_config_files.py
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
- 使用 Markdown 格式编写笔记
- 按照主题和日期组织文件
- 使用标签进行分类管理

### 🛠️ 脚本使用
- 所有脚本都有详细的使用说明
- 运行前请仔细阅读脚本注释
- 建议先在测试环境中验证

### 🎨 图表制作
- Draw.io 文件统一存放在 `diagrams/drawio/` 目录
- 导出的图片保存在 `diagrams/exports/` 目录
- 思维导图使用 `.xmind` 或 `.mm` 格式

### 🎮 游戏资源
- 游戏配置文件定期备份
- 攻略和评测使用 Markdown 格式
- 重要存档及时同步

## 🔧 配置说明

### 环境变量
在 `configs/system/environment/` 目录下配置：
- `dev.env` - 开发环境变量
- `prod.env` - 生产环境变量

### 开发工具配置
- **VS Code**: 配置文件在 `configs/development/vscode/`
- **Git**: 全局配置在 `configs/development/git/`
- **Terminal**: 终端配置在 `configs/development/terminal/`

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

- `#tech` - 技术相关内容
- `#learning` - 学习资料
- `#work` - 工作相关
- `#personal` - 个人内容
- `#gaming` - 游戏相关
- `#tools` - 工具和脚本
- `#config` - 配置文件
- `#template` - 模板文件

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

## 📊 统计信息

*最后更新: 2025-06-26 16:23:02*

- 📁 总目录数: 60+
- 📄 模板文件: 10+
- 🛠️ 脚本工具: 5+
- 📚 文档类型: Markdown, Draw.io, PlantUML

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

*Happy Coding & Learning! 🚀*

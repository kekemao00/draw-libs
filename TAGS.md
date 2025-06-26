# 🏷️ 标签索引系统

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

### 2025-06-26
- 创建初始标签系统
- 定义主要标签分类
- 建立使用规范

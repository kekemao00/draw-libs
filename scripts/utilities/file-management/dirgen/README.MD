## 📖 使用方式

### 1. 脚本文件说明

创建以下 6 个 Python 脚本文件：

1. **`create_directories.py`** - 创建完整目录结构
2. **`create_template_files.py`** - 创建文档模板和别名文件
3. **`create_readme.py`** - 生成带超链接的 README.md
4. **`create_config_files.py`** - 创建项目配置文件
5. **`create_dev_configs.py`** - 创建开发环境配置
6. **`setup.py`** - 主控制脚本（推荐使用）

### 2. 使用方法

#### 方法一：使用主控制脚本（推荐）

```bash
# 运行主设置脚本，自动执行所有步骤
python3 setup.py
```

#### 方法二：单独执行脚本

> `scripts\utilities\file-management\dirgen`

```bash
# 1. 创建目录结构
python3 create_directories.py

# 2. 创建模板文件
python3 create_template_files.py

# 3. 生成 README 文档
python3 create_readme.py

# 4. 创建配置文件
python3 create_config_files.py

# 5. 创建开发环境配置
python3 create_dev_configs.py
```

### 3. 环境要求

- **Python 3.7+**
- **操作系统**: Windows, macOS, Linux
- **权限**: 当前目录的读写权限

### 4. 执行后的结果

- ✅ 完整的目录结构（60+ 个目录）
- ✅ 实用的文档模板（10+ 个模板）
- ✅ 详细的 README.md（带超链接导航）
- ✅ 项目配置文件（Git、VS Code、环境变量等）
- ✅ 开发环境配置（Python、JavaScript、Docker等）
- ✅ 命令别名和自定义脚本

### 5. 后续配置

1. **个性化配置**: 根据个人需求修改配置文件
2. **安装工具**: 安装推荐的开发工具和VS Code扩展
3. **环境变量**: 配置个人的环境变量和API密钥
4. **Git配置**: 更新Git配置中的用户信息

🎉 **现在你就拥有了一个完整、专业的个人数字工作空间！**
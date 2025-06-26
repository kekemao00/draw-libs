创建一个3x-ui的docker-compose配置文件。基于该项目的特点，提供一个完整且实用的配置：


`3x-ui-docker-compose.yaml`



```yaml
version: '3.8'

services:
  3x-ui:
    image: ghcr.io/mhsanaei/3x-ui:latest
    container_name: 3x-ui
    restart: unless-stopped
    
    # 网络模式 - 使用host模式以获得最佳性能
    network_mode: host
    
    # 环境变量配置
    environment:
      - XRAY_VMESS_AEAD_FORCED=false
      - TZ=Asia/Shanghai
    
    # 卷挂载 - 持久化数据
    volumes:
      - ./3x-ui/db/:/etc/x-ui/
      - ./3x-ui/cert/:/root/cert/
      - ./3x-ui/logs/:/var/log/
      - /etc/localtime:/etc/localtime:ro
    
    # 端口映射 (如果不使用host网络模式，取消注释以下端口)
    # ports:
    #   - "2053:2053"     # 3x-ui 管理面板端口
    #   - "443:443"       # HTTPS
    #   - "80:80"         # HTTP
    #   - "8080:8080"     # 可选的代理端口
    #   - "8443:8443"     # 可选的代理端口
    #   - "10000-10010:10000-10010"  # 动态端口范围
    
    # 权限设置
    privileged: true
    
    # 健康检查
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:2053 || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

# 如果不使用host网络模式，可以创建自定义网络
# networks:
#   3x-ui-network:
#     driver: bridge
#     ipam:
#       config:
#         - subnet: 172.20.0.0/16

# 可选：添加数据库服务（如果需要外部数据库）
# services:
#   database:
#     image: sqlite:latest
#     container_name: 3x-ui-db
#     restart: unless-stopped
#     volumes:
#       - ./3x-ui/database:/var/lib/sqlite
#     networks:
#       - 3x-ui-network
```

## 使用说明

### 1. 创建目录结构

```bash
mkdir -p 3x-ui/{db,cert,logs}
chmod 755 3x-ui/{db,cert,logs}
```

### 2. 启动服务

```bash
# 启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f 3x-ui

# 停止服务
docker-compose down
```

### 3. 访问管理面板

- 默认访问地址：`http://your-server-ip:2053`
- 默认用户名：`admin`
- 默认密码：`admin`

### 4. 重要配置说明

**网络模式选择：**

- `network_mode: host`：推荐用于生产环境，性能最佳
- 如需端口隔离，注释掉`network_mode: host`并启用`ports`配置

**数据持久化：**

- `./3x-ui/db/`：存储用户配置和数据库
- `./3x-ui/cert/`：存储SSL证书
- `./3x-ui/logs/`：存储日志文件

**安全建议：**

1. 首次登录后立即修改默认用户名和密码
2. 配置防火墙规则，限制管理面板访问
3. 启用HTTPS访问
4. 定期备份配置文件

### 5. 常用管理命令

```bash
# 进入容器
docker exec -it 3x-ui bash

# 重置管理员账户
docker exec -it 3x-ui x-ui setting -username admin -password admin

# 查看容器状态
docker-compose ps

# 更新到最新版本
docker-compose pull && docker-compose up -d
```

这个配置文件提供了完整的3x-ui部署方案，包含了数据持久化、健康检查和安全配置。您可以根据实际需求调整端口映射和网络配置。
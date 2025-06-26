# 3X-UI一键诊断脚本



```bash
cat > /tmp/3xui_diagnosis.sh << 'EOF'
#!/bin/bash

# 3X-UI 一键诊断脚本
# Author: Monica Assistant
# Date: $(date +%Y-%m-%d)

echo "======================================"
echo "🔍 3X-UI 系统诊断脚本"
echo "======================================"
echo "开始时间: $(date)"
echo ""

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
  echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
  echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
  echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
  echo -e "${RED}[ERROR]${NC} $1"
}

# 检查是否为root用户
check_root() {
  if [[ $EUID -ne 0 ]]; then
      log_error "请使用root用户运行此脚本"
      exit 1
  fi
}

# 系统信息检查
check_system_info() {
  echo ""
  echo "=== 📋 系统信息 ==="
  log_info "操作系统: $(cat /etc/os-release | grep PRETTY_NAME | cut -d'"' -f2)"
  log_info "内核版本: $(uname -r)"
  log_info "系统架构: $(uname -m)"
  log_info "系统时间: $(date)"
  log_info "系统负载: $(uptime | awk -F'load average:' '{print $2}')"
  log_info "内存使用: $(free -h | grep Mem | awk '{print $3"/"$2}')"
  log_info "磁盘使用: $(df -h / | tail -1 | awk '{print $3"/"$2" ("$5")"}')"
}

# Docker检查
check_docker() {
  echo ""
  echo "=== 🐳 Docker 状态检查 ==="
  
  if command -v docker &> /dev/null; then
      log_success "Docker 已安装"
      log_info "Docker 版本: $(docker --version)"
      
      if systemctl is-active --quiet docker; then
          log_success "Docker 服务运行正常"
      else
          log_error "Docker 服务未运行"
          systemctl status docker --no-pager -l
      fi
      
      # 检查3X-UI容器
      echo ""
      log_info "检查3X-UI相关容器:"
      docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E "(3x-ui|xray|v2ray)" || log_warning "未找到3X-UI相关容器"
      
  else
      log_error "Docker 未安装"
  fi
}

# 网络检查
check_network() {
  echo ""
  echo "=== 🌐 网络状态检查 ==="
  
  # 检查网络接口
  log_info "网络接口信息:"
  ip addr show | grep -E "(inet |UP)" | grep -v "127.0.0.1"
  
  # 检查DNS
  echo ""
  log_info "DNS解析测试:"
  if nslookup google.com &> /dev/null; then
      log_success "DNS解析正常"
  else
      log_error "DNS解析失败"
  fi
  
  # 检查外网连接
  log_info "外网连接测试:"
  if ping -c 3 8.8.8.8 &> /dev/null; then
      log_success "外网连接正常"
  else
      log_error "外网连接失败"
  fi
}

# 端口检查
check_ports() {
  echo ""
  echo "=== 🚪 端口监听检查 ==="
  
  log_info "当前监听的端口:"
  netstat -tlnp | grep LISTEN | head -20
  
  echo ""
  log_info "常见3X-UI端口检查:"
  common_ports=(2053 2083 2087 8080 8443 10000 54321)
  
  for port in "${common_ports[@]}"; do
      if netstat -tlnp | grep ":$port " &> /dev/null; then
          log_success "端口 $port 正在监听"
      else
          log_warning "端口 $port 未监听"
      fi
  done
}

# 防火墙检查
check_firewall() {
  echo ""
  echo "=== 🔥 防火墙状态检查 ==="
  
  # 检查firewalld
  if systemctl is-active --quiet firewalld; then
      log_info "Firewalld 状态: 运行中"
      firewall-cmd --list-all 2>/dev/null || log_warning "无法获取firewalld规则"
  else
      log_info "Firewalld 状态: 未运行"
  fi
  
  # 检查ufw
  if command -v ufw &> /dev/null; then
      log_info "UFW 状态: $(ufw status | head -1)"
  fi
  
  # 检查iptables
  echo ""
  log_info "IPTables 规则 (前10条):"
  iptables -L -n | head -15
}

# 3X-UI日志检查
check_3xui_logs() {
  echo ""
  echo "=== 📝 3X-UI 日志检查 ==="
  
  log_dirs=(
      "/opt/3x-ui-docker/3x-ui/logs"
      "/opt/3x-ui/logs"
      "/usr/local/3x-ui/logs"
  )
  
  for log_dir in "${log_dirs[@]}"; do
      if [[ -d "$log_dir" ]]; then
          log_success "找到日志目录: $log_dir"
          
          echo "日志文件列表:"
          ls -la "$log_dir"
          
          echo ""
          log_info "检查主要日志文件内容:"
          
          # 检查各个日志文件
          for log_file in "$log_dir"/*.log; do
              if [[ -f "$log_file" && -s "$log_file" ]]; then
                  echo "--- $(basename $log_file) (最后10行) ---"
                  tail -10 "$log_file" 2>/dev/null || log_warning "无法读取 $log_file"
                  echo ""
              fi
          done
          break
      fi
  done
  
  if [[ ! -d "/opt/3x-ui-docker/3x-ui/logs" && ! -d "/opt/3x-ui/logs" && ! -d "/usr/local/3x-ui/logs" ]]; then
      log_error "未找到3X-UI日志目录"
  fi
}

# Docker容器日志检查
check_docker_logs() {
  echo ""
  echo "=== 📋 Docker 容器日志 ==="
  
  if command -v docker &> /dev/null; then
      # 查找3X-UI相关容器
      containers=$(docker ps -a --format "{{.Names}}" | grep -E "(3x-ui|xray|v2ray)" | head -3)
      
      if [[ -n "$containers" ]]; then
          for container in $containers; do
              log_info "容器 $container 日志 (最后20行):"
              docker logs --tail 20 "$container" 2>&1 || log_warning "无法获取容器 $container 的日志"
              echo ""
          done
      else
          log_warning "未找到3X-UI相关的Docker容器"
      fi
  fi
}

# 配置文件检查
check_config_files() {
  echo ""
  echo "=== ⚙️ 配置文件检查 ==="
  
  config_paths=(
      "/opt/3x-ui-docker/3x-ui/x-ui.db"
      "/opt/3x-ui/bin/x-ui.db"
      "/usr/local/3x-ui/bin/x-ui.db"
      "/opt/3x-ui-docker/3x-ui/config.json"
      "/etc/3x-ui/config.json"
  )
  
  for config_path in "${config_paths[@]}"; do
      if [[ -f "$config_path" ]]; then
          log_success "找到配置文件: $config_path"
          ls -la "$config_path"
      fi
  done
}

# 性能检查
check_performance() {
  echo ""
  echo "=== ⚡ 性能检查 ==="
  
  log_info "CPU使用率:"
  top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1
  
  log_info "内存详情:"
  free -h
  
  log_info "磁盘IO:"
  iostat 1 1 2>/dev/null | tail -n +4 || log_warning "iostat 命令不可用"
  
  log_info "网络连接数:"
  ss -s 2>/dev/null || netstat -s | grep -E "(connections|packets)"
}

# 生成诊断报告
generate_report() {
  echo ""
  echo "=== 📊 诊断总结 ==="
  
  report_file="/tmp/3xui_diagnosis_$(date +%Y%m%d_%H%M%S).txt"
  
  {
      echo "3X-UI 诊断报告"
      echo "生成时间: $(date)"
      echo "服务器IP: $(curl -s ifconfig.me 2>/dev/null || echo "无法获取")"
      echo ""
      echo "=== 建议检查项目 ==="
      echo "1. 确认Docker容器运行状态"
      echo "2. 检查防火墙端口开放情况"
      echo "3. 验证入站配置正确性"
      echo "4. 查看详细错误日志"
      echo "5. 测试客户端连接配置"
  } > "$report_file"
  
  log_success "诊断报告已保存至: $report_file"
}

# 主函数
main() {
  check_root
  check_system_info
  check_docker
  check_network
  check_ports
  check_firewall
  check_3xui_logs
  check_docker_logs
  check_config_files
  check_performance
  generate_report
  
  echo ""
  echo "======================================"
  log_success "🎉 诊断完成!"
  echo "======================================"
  echo "如果问题仍未解决，请将诊断结果发送给技术支持"
  echo ""
}

# 运行主函数
main "$@"
EOF

chmod +x /tmp/3xui_diagnosis.sh

sudo /tmp/3xui_diagnosis.sh

```


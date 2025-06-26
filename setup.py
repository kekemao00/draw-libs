#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Personal Workspace Setup - Main Control Script
个人工作空间设置 - 主控制脚本
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

def print_banner():
  """打印欢迎横幅"""
  banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        🗂️  Personal Workspace Setup Tool 🗂️                  ║
║                                                              ║
║        个人数字工作空间自动化设置工具                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
  print(banner)
  print(f"📅 当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  print(f"📁 当前目录: {os.getcwd()}")
  print("=" * 66)

def run_script(script_name, description):
  """运行指定的脚本"""
  try:
      print(f"\n🚀 开始执行: {description}")
      print("-" * 50)
      
      result = subprocess.run([sys.executable, script_name], 
                            capture_output=False, 
                            text=True)
      
      if result.returncode == 0:
          print(f"✅ {description} - 执行成功!")
      else:
          print(f"❌ {description} - 执行失败! (退出码: {result.returncode})")
          return False
          
  except FileNotFoundError:
      print(f"❌ 脚本文件未找到: {script_name}")
      return False
  except Exception as e:
      print(f"❌ 执行脚本时发生错误: {e}")
      return False
  
  return True

def check_python_version():
  """检查 Python 版本"""
  version = sys.version_info
  if version.major < 3 or (version.major == 3 and version.minor < 7):
      print("❌ 需要 Python 3.7 或更高版本!")
      print(f"   当前版本: Python {version.major}.{version.minor}.{version.micro}")
      return False
  
  print(f"✅ Python 版本检查通过: {version.major}.{version.minor}.{version.micro}")
  return True

def main():
  """主函数"""
  print_banner()
  
  # 检查 Python 版本
  if not check_python_version():
      sys.exit(1)
  
  # 定义要执行的脚本列表
  scripts = [
      ("create_directories.py", "创建目录结构"),
      ("create_template_files.py", "创建模板文件"),
      ("create_readme.py", "生成 README 文档"),
      ("create_config_files.py", "创建配置文件"),
      ("create_dev_configs.py", "创建开发环境配置")
  ]
  
  print(f"\n📋 将要执行 {len(scripts)} 个设置脚本:")
  for i, (script, desc) in enumerate(scripts, 1):
      print(f"   {i}. {desc} ({script})")
  
  # 询问用户确认
  print("\n❓ 是否继续执行所有脚本? (y/n): ", end="")
  choice = input().lower().strip()
  
  if choice not in ['y', 'yes', '是', '确认']:
      print("🚫 用户取消操作")
      sys.exit(0)
  
  print("\n🎯 开始执行工作空间设置...")
  print("=" * 66)
  
  success_count = 0
  failed_scripts = []
  
  # 执行所有脚本
  for script_name, description in scripts:
      if run_script(script_name, description):
          success_count += 1
      else:
          failed_scripts.append((script_name, description))
  
  # 显示执行结果
  print("\n" + "=" * 66)
  print("📊 执行结果统计:")
  print(f"   ✅ 成功执行: {success_count} 个脚本")
  print(f"   ❌ 执行失败: {len(failed_scripts)} 个脚本")
  
  if failed_scripts:
      print("\n❌ 失败的脚本:")
      for script, desc in failed_scripts:
          print(f"   - {desc} ({script})")
      print("\n💡 建议:")
      print("   1. 检查失败脚本的错误信息")
      print("   2. 手动执行失败的脚本")
      print("   3. 确保有足够的文件系统权限")
  
  if success_count == len(scripts):
      print("\n🎉 恭喜! 个人工作空间设置完成!")
      print("\n📚 下一步操作:")
      print("   1. 查看生成的 README.md 文件")
      print("   2. 根据需要修改配置文件")
      print("   3. 安装推荐的开发工具和扩展")
      print("   4. 开始使用你的个人工作空间!")
      
      print("\n🔗 快速链接:")
      print("   - 📖 README.md - 完整使用指南")
      print("   - 🏷️ TAGS.md - 标签索引系统")
      print("   - 🔍 SEARCH.md - 搜索使用技巧")
      print("   - 📋 CHANGELOG.md - 更新日志")
  else:
      print("\n⚠️  设置过程中遇到一些问题，请检查上述错误信息")
  
  print("\n" + "=" * 66)
  print("感谢使用 Personal Workspace Setup Tool! 🚀")

if __name__ == "__main__":
  try:
      main()
  except KeyboardInterrupt:
      print("\n\n⚠️  用户中断操作")
      sys.exit(1)
  except Exception as e:
      print(f"\n❌ 发生未预期的错误: {e}")
      sys.exit(1)
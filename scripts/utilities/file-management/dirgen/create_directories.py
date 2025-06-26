#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Personal Workspace Directory Structure Creator
创建个人工作空间目录结构的脚本
"""

import os
import sys
from pathlib import Path

def create_directory_structure():
  """创建完整的目录结构"""
  
  # 定义目录结构
  directories = [
      # 📚 notes/
      "notes/tech/programming",
      "notes/tech/tools", 
      "notes/tech/frameworks",
      "notes/tech/troubleshooting",
      "notes/learning/courses",
      "notes/learning/books",
      "notes/learning/tutorials", 
      "notes/learning/research",
      "notes/work/projects",
      "notes/work/meetings",
      "notes/work/ideas",
      "notes/personal/daily",
      "notes/personal/goals",
      "notes/personal/reflections",
      
      # 🛠️ scripts/
      "scripts/install/dev-environment",
      "scripts/install/applications",
      "scripts/install/system-setup",
      "scripts/automation/backup",
      "scripts/automation/deployment", 
      "scripts/automation/monitoring",
      "scripts/automation/maintenance",
      "scripts/utilities/file-management",
      "scripts/utilities/data-processing",
      "scripts/utilities/system-tools",
      "scripts/aliases",
      
      # 🎨 diagrams/
      "diagrams/drawio/architecture",
      "diagrams/drawio/flowcharts",
      "diagrams/drawio/network",
      "diagrams/drawio/ui-mockups",
      "diagrams/mindmaps/learning",
      "diagrams/mindmaps/projects", 
      "diagrams/mindmaps/brainstorming",
      "diagrams/plantuml",
      "diagrams/exports",
      
      # 🎮 gaming/
      "gaming/guides/walkthroughs",
      "gaming/guides/strategies",
      "gaming/guides/tips-tricks",
      "gaming/configs/game-settings",
      "gaming/configs/mods",
      "gaming/configs/keybindings",
      "gaming/reviews/game-reviews",
      "gaming/reviews/hardware-reviews",
      "gaming/reviews/recommendations",
      "gaming/saves",
      
      # ⚙️ configs/
      "configs/development/vscode",
      "configs/development/git",
      "configs/development/terminal",
      "configs/development/editors",
      "configs/system/dotfiles",
      "configs/system/environment", 
      "configs/system/startup",
      "configs/applications/browsers",
      "configs/applications/media",
      "configs/applications/productivity",
      
      # 📋 templates/
      "templates/documents",
      "templates/code/project-structure",
      "templates/code/code-snippets",
      "templates/configs/docker",
      "templates/configs/ci-cd",
      "templates/configs/deployment",
      
      # 🔗 resources/
      "resources/bookmarks",
      "resources/cheatsheets",
      "resources/references",
      "resources/downloads",
      
      # 📊 tracking/
      "tracking/habits",
      "tracking/goals", 
      "tracking/learning-progress",
      "tracking/project-status",
      
      # 🗄️ archive/
      "archive/old-projects",
      "archive/deprecated-scripts",
      "archive/historical-notes"
  ]
  
  print("🚀 开始创建个人工作空间目录结构...")
  print("=" * 50)
  
  created_count = 0
  skipped_count = 0
  
  for directory in directories:
      dir_path = Path(directory)
      
      if dir_path.exists():
          print(f"⏭️  跳过已存在的目录: {directory}")
          skipped_count += 1
      else:
          try:
              dir_path.mkdir(parents=True, exist_ok=True)
              print(f"✅ 创建目录: {directory}")
              created_count += 1
          except Exception as e:
              print(f"❌ 创建目录失败 {directory}: {e}")
  
  print("=" * 50)
  print(f"🎉 目录创建完成!")
  print(f"📊 统计信息:")
  print(f"   - 新创建: {created_count} 个目录")
  print(f"   - 已跳过: {skipped_count} 个目录")
  print(f"   - 总计: {len(directories)} 个目录")

if __name__ == "__main__":
  try:
      create_directory_structure()
  except KeyboardInterrupt:
      print("\n\n⚠️  操作被用户中断")
      sys.exit(1)
  except Exception as e:
      print(f"\n❌ 发生错误: {e}")
      sys.exit(1)
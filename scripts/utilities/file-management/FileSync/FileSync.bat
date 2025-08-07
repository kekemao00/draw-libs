@echo off
setlocal enabledelayedexpansion

:: ==========================================
:: 配置区域 - 根据需要修改这里的参数
:: ==========================================
set "SOURCE_DIR=AAA"
set "TARGET_DIR=BBB"
set "FILE_NAME=file.bin"
set "SERVICE_NAME=FileSyncService"
set "SERVICE_DISPLAY_NAME=文件同步服务"
set "LOG_DIR=%~dp0logs"
set "LOG_FILE=%LOG_DIR%\sync_%date:~0,4%%date:~5,2%%date:~8,2%.log"
set "PID_FILE=%~dp0sync.pid"
set "CONFIG_FILE=%~dp0sync.config"

:: 创建日志目录
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

:: 检查管理员权限
net session >nul 2>&1
if !errorlevel! neq 0 (
  echo.
  echo ==========================================
  echo 错误: 需要管理员权限
  echo ==========================================
  echo 请右键点击此脚本，选择"以管理员身份运行"
  echo.
  pause
  exit /b 1
)

:: 检查运行参数
if "%1"=="install" goto INSTALL_SERVICE
if "%1"=="uninstall" goto UNINSTALL_SERVICE
if "%1"=="start" goto START_SERVICE
if "%1"=="stop" goto STOP_SERVICE
if "%1"=="restart" goto RESTART_SERVICE
if "%1"=="status" goto CHECK_STATUS
if "%1"=="logs" goto VIEW_LOGS
if "%1"=="config" goto EDIT_CONFIG
if "%1"=="service" goto RUN_AS_SERVICE

:: 默认显示主菜单
:SHOW_MENU
cls
echo.
echo ==========================================
echo    Robocopy 文件同步服务管理器 v2.0
echo ==========================================
echo.
echo 当前配置:
echo   源目录: %SOURCE_DIR%
echo   目标目录: %TARGET_DIR%
echo   同步文件: %FILE_NAME%
echo   服务名称: %SERVICE_NAME%
echo   日志目录: %LOG_DIR%
echo.
echo 操作选项:
echo   [1] 安装服务
echo   [2] 卸载服务
echo   [3] 启动服务
echo   [4] 停止服务
echo   [5] 重启服务
echo   [6] 查看状态
echo   [7] 查看日志
echo   [8] 编辑配置
echo   [9] 测试同步
echo   [0] 退出
echo.
echo ==========================================
set /p choice=请选择操作 (0-9): 

if "%choice%"=="1" goto INSTALL_SERVICE
if "%choice%"=="2" goto UNINSTALL_SERVICE
if "%choice%"=="3" goto START_SERVICE
if "%choice%"=="4" goto STOP_SERVICE
if "%choice%"=="5" goto RESTART_SERVICE
if "%choice%"=="6" goto CHECK_STATUS
if "%choice%"=="7" goto VIEW_LOGS
if "%choice%"=="8" goto EDIT_CONFIG
if "%choice%"=="9" goto TEST_SYNC
if "%choice%"=="0" goto END

echo 无效选择，请重新输入...
timeout /t 2 >nul
goto SHOW_MENU

:: ==========================================
:: 服务管理功能
:: ==========================================

:INSTALL_SERVICE
echo.
echo 正在安装文件同步服务...
call :LOG "开始安装服务: %SERVICE_NAME%"

:: 检查服务是否已存在
sc query "%SERVICE_NAME%" >nul 2>&1
if !errorlevel! equ 0 (
  echo 警告: 服务已存在，正在删除旧服务...
  sc stop "%SERVICE_NAME%" >nul 2>&1
  timeout /t 3 >nul
  sc delete "%SERVICE_NAME%" >nul 2>&1
  timeout /t 2 >nul
)

:: 安装新服务
sc create "%SERVICE_NAME%" ^
  binpath= "cmd /c \"%~f0\" service" ^
  start= auto ^
  DisplayName= "%SERVICE_DISPLAY_NAME%" ^
  depend= "Tcpip/Afd" >nul 2>&1

if !errorlevel! equ 0 (
  echo ✓ 服务安装成功！
  call :LOG "服务安装成功: %SERVICE_NAME%"
  
  :: 设置服务描述
  sc description "%SERVICE_NAME%" "自动同步 %SOURCE_DIR%\%FILE_NAME% 到 %TARGET_DIR%" >nul 2>&1
  
  echo.
  echo 是否立即启动服务？ (Y/N)
  set /p start_now=
  if /i "!start_now!"=="Y" goto START_SERVICE
) else (
  echo ✗ 服务安装失败！
  call :LOG "服务安装失败: %SERVICE_NAME%"
)

echo.
pause
goto SHOW_MENU

:UNINSTALL_SERVICE
echo.
echo 正在卸载文件同步服务...
call :LOG "开始卸载服务: %SERVICE_NAME%"

sc stop "%SERVICE_NAME%" >nul 2>&1
timeout /t 3 >nul
sc delete "%SERVICE_NAME%" >nul 2>&1

if !errorlevel! equ 0 (
  echo ✓ 服务卸载成功！
  call :LOG "服务卸载成功: %SERVICE_NAME%"
  
  :: 清理文件
  if exist "%PID_FILE%" del "%PID_FILE%"
) else (
  echo ✗ 服务卸载失败！
  call :LOG "服务卸载失败: %SERVICE_NAME%"
)

echo.
pause
goto SHOW_MENU

:START_SERVICE
echo.
echo 正在启动文件同步服务...
call :LOG "启动服务: %SERVICE_NAME%"

sc start "%SERVICE_NAME%" >nul 2>&1
if !errorlevel! equ 0 (
  echo ✓ 服务启动成功！
  call :LOG "服务启动成功: %SERVICE_NAME%"
  timeout /t 2 >nul
  goto CHECK_STATUS
) else (
  echo ✗ 服务启动失败！
  call :LOG "服务启动失败: %SERVICE_NAME%"
)

echo.
pause
goto SHOW_MENU

:STOP_SERVICE
echo.
echo 正在停止文件同步服务...
call :LOG "停止服务: %SERVICE_NAME%"

sc stop "%SERVICE_NAME%" >nul 2>&1
if !errorlevel! equ 0 (
  echo ✓ 服务停止成功！
  call :LOG "服务停止成功: %SERVICE_NAME%"
  if exist "%PID_FILE%" del "%PID_FILE%"
) else (
  echo ✗ 服务停止失败！
  call :LOG "服务停止失败: %SERVICE_NAME%"
)

echo.
pause
goto SHOW_MENU

:RESTART_SERVICE
echo.
echo 正在重启文件同步服务...
call :STOP_SERVICE
timeout /t 3 >nul
call :START_SERVICE
goto SHOW_MENU

:CHECK_STATUS
echo.
echo ==========================================
echo 服务状态检查
echo ==========================================

:: 检查服务状态
sc query "%SERVICE_NAME%" >nul 2>&1
if !errorlevel! neq 0 (
  echo ✗ 服务未安装
  echo.
  pause
  goto SHOW_MENU
)

:: 获取详细状态
for /f "tokens=2 delims=:" %%i in ('sc query "%SERVICE_NAME%" ^| find "STATE"') do (
  set "SERVICE_STATE=%%i"
  set "SERVICE_STATE=!SERVICE_STATE: =!"
)

echo 服务名称: %SERVICE_NAME%
echo 显示名称: %SERVICE_DISPLAY_NAME%
echo 当前状态: !SERVICE_STATE!

if exist "%PID_FILE%" (
  echo 运行时间: 
  for /f %%i in (%PID_FILE%) do echo   启动于: %%i
)

echo 源目录: %SOURCE_DIR%
echo 目标目录: %TARGET_DIR%
echo 同步文件: %FILE_NAME%
echo 日志文件: %LOG_FILE%

:: 检查目录状态
if exist "%SOURCE_DIR%" (
  echo ✓ 源目录存在
) else (
  echo ✗ 源目录不存在
)

if exist "%TARGET_DIR%" (
  echo ✓ 目标目录存在
) else (
  echo ✗ 目标目录不存在
)

if exist "%SOURCE_DIR%\%FILE_NAME%" (
  echo ✓ 源文件存在
  for %%F in ("%SOURCE_DIR%\%FILE_NAME%") do (
      echo   文件大小: %%~zF 字节
      echo   修改时间: %%~tF
  )
) else (
  echo ✗ 源文件不存在
)

if exist "%TARGET_DIR%\%FILE_NAME%" (
  echo ✓ 目标文件存在
  for %%F in ("%TARGET_DIR%\%FILE_NAME%") do (
      echo   文件大小: %%~zF 字节
      echo   修改时间: %%~tF
  )
) else (
  echo ✗ 目标文件不存在
)

echo.
pause
goto SHOW_MENU

:VIEW_LOGS
echo.
echo ==========================================
echo 查看同步日志
echo ==========================================

if exist "%LOG_FILE%" (
  echo 最新日志内容 (最后20行):
  echo ------------------------------------------
  
  :: 显示最后20行日志
  powershell -command "Get-Content '%LOG_FILE%' | Select-Object -Last 20"
  
  echo ------------------------------------------
  echo.
  echo 完整日志文件: %LOG_FILE%
  echo.
  echo [1] 打开完整日志文件
  echo [2] 清空日志文件
  echo [3] 返回主菜单
  echo.
  set /p log_choice=请选择操作: 
  
  if "!log_choice!"=="1" (
      start notepad "%LOG_FILE%"
  ) else if "!log_choice!"=="2" (
      echo. > "%LOG_FILE%"
      echo 日志文件已清空
      timeout /t 2 >nul
  )
) else (
  echo 日志文件不存在: %LOG_FILE%
  echo.
  pause
)

goto SHOW_MENU

:TEST_SYNC
echo.
echo ==========================================
echo 测试同步功能
echo ==========================================

call :CHECK_ENVIRONMENT
if !errorlevel! neq 0 (
  echo 环境检查失败，无法执行测试
  pause
  goto SHOW_MENU
)

echo 执行一次性同步测试...
robocopy "%SOURCE_DIR%" "%TARGET_DIR%" "%FILE_NAME%" /R:1 /W:1 /NP /NDL /NC /NS /NJH

set "SYNC_RESULT=!errorlevel!"
if !SYNC_RESULT! leq 1 (
  echo ✓ 同步测试成功！
) else if !SYNC_RESULT! leq 3 (
  echo ✓ 同步测试完成（有额外文件复制）
) else (
  echo ✗ 同步测试失败，错误代码: !SYNC_RESULT!
)

echo.
pause
goto SHOW_MENU

:: ==========================================
:: 服务运行模式
:: ==========================================

:RUN_AS_SERVICE
:: 这是服务实际运行的代码
call :LOG "=== 文件同步服务启动 ==="

:: 记录启动时间
echo %date% %time% > "%PID_FILE%"

:: 环境检查
call :CHECK_ENVIRONMENT
if !errorlevel! neq 0 (
  call :LOG "环境检查失败，服务退出"
  exit /b 1
)

:: 服务主循环
:SERVICE_LOOP
  call :LOG "开始监控模式..."
  
  :: 执行robocopy监控
  robocopy "%SOURCE_DIR%" "%TARGET_DIR%" "%FILE_NAME%" ^
      /MON:1 /MOT:1 ^
      /R:999 /W:5 ^
      /LOG+:"%LOG_FILE%" ^
      /NP /NDL /NC /NS /NJH
  
  :: 检查退出代码
  set "EXIT_CODE=!errorlevel!"
  call :LOG "Robocopy退出，代码: !EXIT_CODE!"
  
  :: 如果是严重错误，等待后重试
  if !EXIT_CODE! gtr 7 (
      call :LOG "发生严重错误，等待30秒后重试..."
      timeout /t 30 /nobreak >nul 2>&1
  ) else (
      call :LOG "正常退出，等待5秒后重启监控..."
      timeout /t 5 /nobreak >nul 2>&1
  )
  
  :: 检查服务是否应该停止
  sc query "%SERVICE_NAME%" | find "STOP_PENDING" >nul 2>&1
  if !errorlevel! equ 0 (
      call :LOG "收到停止信号，服务退出"
      goto SERVICE_EXIT
  )
  
  goto SERVICE_LOOP

:SERVICE_EXIT
call :LOG "=== 文件同步服务停止 ==="
if exist "%PID_FILE%" del "%PID_FILE%"
exit /b 0

:: ==========================================
:: 辅助函数
:: ==========================================

:CHECK_ENVIRONMENT
  if not exist "%SOURCE_DIR%" (
      call :LOG "错误: 源目录不存在 - %SOURCE_DIR%"
      exit /b 1
  )
  
  if not exist "%TARGET_DIR%" (
      mkdir "%TARGET_DIR%" 2>nul
      if !errorlevel! neq 0 (
          call :LOG "错误: 无法创建目标目录 - %TARGET_DIR%"
          exit /b 1
      )
      call :LOG "创建目标目录: %TARGET_DIR%"
  )
  
  exit /b 0

:LOG
  set "MSG=[%date% %time%] %~1"
  echo !MSG! >> "%LOG_FILE%"
  goto :eof

:EDIT_CONFIG
echo.
echo ==========================================
echo 编辑配置
echo ==========================================
echo 当前配置:
echo 1. 源目录: %SOURCE_DIR%
echo 2. 目标目录: %TARGET_DIR%
echo 3. 文件名: %FILE_NAME%
echo 4. 服务名: %SERVICE_NAME%
echo.
echo 注意: 修改配置需要重新安装服务才能生效
echo 请直接编辑脚本文件中的配置区域
echo.
pause
goto SHOW_MENU

:END
exit /b 0
@echo off
chcp 65001 > nul  
REM UTF-8 코드 페이지 설정

set /p hours="알람을 울릴 시를 입력하세요 (0-23): "
set /p minutes="알람을 울릴 분을 입력하세요 (0-59): "
set /p seconds="알람을 울릴 초를 입력하세요 (0-59): "

set /a total_seconds=(%hours% * 3600) + (%minutes% * 60) + %seconds%

:loop
if %total_seconds% lss 0 goto alarm

set /a hours_remaining=%total_seconds% / 3600
set /a minutes_remaining=(%total_seconds% %% 3600) / 60
set /a seconds_remaining=%total_seconds% %% 60

REM 남은 시간을 두 자리로 포맷
setlocal enabledelayedexpansion
set "formatted_hours=0!hours_remaining!"
set "formatted_minutes=0!minutes_remaining!"
set "formatted_seconds=0!seconds_remaining!"
set "formatted_hours=!formatted_hours:~-2!"
set "formatted_minutes=!formatted_minutes:~-2!"
set "formatted_seconds=!formatted_seconds:~-2!"
endlocal & set "formatted_hours=%formatted_hours%" & set "formatted_minutes=%formatted_minutes%" & set "formatted_seconds=%formatted_seconds%"

cls
echo 남은 시간: %formatted_hours%시 %formatted_minutes%분 %formatted_seconds%초
timeout /t 1 >nul
set /a total_seconds-=1
goto loop

:alarm
cls
echo 알람! 알람! 알람!
powershell -c (New-Object Media.SoundPlayer "C:\Windows\Media\notify.wav").PlaySync()

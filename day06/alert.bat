@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul 
rem  UTF-8 인코딩 설정

:: 프로그램 시작 전에 엔터를 누르도록 요청
echo 알람 프로그램을 시작하려면 엔터 키를 누르세요...
pause >nul

:: 사용자로부터 알람 시간을 시, 분, 초로 각각 입력받기
set /p hour=알람 시를 입력하세요 (기본값: 0): 
if "%hour%"=="" set hour=0

set /p minute=알람 분을 입력하세요 (기본값: 0): 
if "%minute%"=="" set minute=0

set /p second=알람 초를 입력하세요 (기본값: 0): 
if "%second%"=="" set second=0

echo 알람 시간이 설정되었습니다: !hour!시 !minute!분 !second!초

:loop
:: 현재 시간 가져오기
echo 현재 시간을 가져오는 중...
for /f "tokens=1,2,3 delims=:" %%a in ('time /t') do (
    set currentHour=%%a
    set currentMinute=%%b
    set currentSecond=%%c
)
echo 현재 시간: !currentHour!시 !currentMinute!분 !currentSecond!초

:: 남은 시간 계산
set /a remainingSeconds=(%hour%*3600 + %minute%*60 + %second%) - (%currentHour%*3600 + %currentMinute%*60 + %currentSecond%)

if !remainingSeconds! gtr 0 (
    set /a hoursRemaining=!remainingSeconds!/3600
    set /a minutesRemaining=(!remainingSeconds!%%3600)/60
    set /a secondsRemaining=!remainingSeconds!%%60
    echo 남은 시간: !hoursRemaining!시간 !minutesRemaining!분 !secondsRemaining!초
    timeout /t 1 >nul
    goto loop
)

:: 알람 소리 재생
echo 알람이 울립니다!
echo.
echo "띵동! 알람 시간입니다!"
:: 소리 재생 (Windows 기본 소리)
echo ^G

:: 사용자가 키를 누를 때까지 대기
echo 계속하려면 아무 키나 누르세요...
pause >nul
exit

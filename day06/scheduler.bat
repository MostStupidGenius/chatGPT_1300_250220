@echo off
chcp 65001 > nul  
REM UTF-8 코드 페이지 설정

REM 사용자로부터 시와 분을 입력받습니다.
set /p hours=종료할 시간을 입력하세요 (시): 
set /p minutes=종료할 시간을 입력하세요 (분): 

REM 입력받은 시와 분을 초로 변환합니다.
set /a total_seconds=(%hours% * 3600) + (%minutes% * 60)

REM 지정한 시간 후에 컴퓨터를 종료합니다.
timeout /t %total_seconds% /nobreak
shutdown /s /t 0

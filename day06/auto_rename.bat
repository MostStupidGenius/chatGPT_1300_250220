@echo off
chcp 65001 > nul 
rem  UTF-8 인코딩 설정
setlocal enabledelayedexpansion

:: 폴더 경로 입력
set /p folderPath="폴더 경로를 입력하세요: "

:: 폴더 이름 추출
for %%F in ("%folderPath%") do set "folderName=%%~nF"

:: 원하는 파일 이름의 첫 부분 입력
set /p customName="원하는 파일 이름의 첫 부분을 입력하세요 (엔터를 치면 폴더 이름 사용): "

:: 파일 이름 변경
set count=1
for %%G in ("%folderPath%\*") do (
    set "extension=%%~xG"  
    rem 파일 확장자 저장
    
    if "!customName!"=="" (
        set "newName=!folderName!"
    ) else (
        set "newName=!customName!"
    )
    
    if !count! lss 10 (
        set "newName=!newName!00!count!"
    ) else if !count! lss 100 (
        set "newName=!newName!0!count!"
    ) else (
        set "newName=!newName!!count!"
    )
    
    set "newName=!newName!!extension!"
    rem 확장자 추가
    ren "%%G" "!newName!"
    set /a count+=1
)

echo 파일 이름 변경 완료!
pause
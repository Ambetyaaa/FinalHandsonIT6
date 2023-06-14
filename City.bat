@echo off
setlocal enabledelayedexpansion
start "Api" cmd /k "python Final_Api.py"


:main
cls
curl  http://127.0.0.1:5000/

choice /c 12345 /N

if %ERRORLEVEL% == 1 (
	cls
	goto add
)
if %ERRORLEVEL% == 2 (
	cls
	goto retrieve
)
if %ERRORLEVEL% == 3 (
	cls
	goto update
)
if %ERRORLEVEL% == 4 (
	cls
	goto delete
)
if %ERRORLEVEL% == 5 (
	cls
	goto end
)

goto end

:add
cls
set /p "Name=Enter Name name: "
set /p "Contry_Code=Enter Country_Code: "
set /p "District=Enter District: "

set "json={\"Name\":\"%Name%\",\"Country_Code  \":\"%Country_Code%\",\"District\":\"%District%\"}

curl -X POST -H "Content-Type: application/json" -d "%json%" http://127.0.0.1:5000/City
:retrieve
:update
:delete
:end
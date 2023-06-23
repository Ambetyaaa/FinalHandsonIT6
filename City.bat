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
	goto reading
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
set /p "Name=Enter City Name: "
set /p "Contry_Code=Enter CountryCode (e.g: PHP, USA, KKK): "
set /p "District=Enter District: "



set "json_db={\"Name\":\"%Name%\",\"CountryCode\":\"%CountryCode%\",\"District\":\"%District%\"}"

curl --fail -X POST -H "Content-Type: application/json" -d "%json_db%" http://127.0.0.1:5000/city

if %ERRORLEVEL% NEQ 0 (
    echo An error occurred while adding the city.
    pause
    goto :main
)
goto :main

rem View on the table
:reading
cls
echo:
echo        SELECT 
echo:
echo (1) Search a City
echo (2) Retrieve All city
echo (3) Back 
echo:
choice /c 123 /N 

if %ERRORLEVEL% == 1 (
	goto :Find
)
if %ERRORLEVEL% == 2 (
	goto :View
)

if %ERRORLEVEL% == 3 (
	goto :main
)

rem View all the and choose and format
:View 
cls

echo       CHOOSE FORMAT

echo (1) XML
echo (2) JSON
echo (3) CANCEL

choice /c 123 /N 

if %ERRORLEVEL% == 1 (
    cls
    curl  -X GET http://127.0.0.1:5000/city?format=xml
    pause
	goto reading
)
if %ERRORLEVEL% == 2 (
    cls
    curl  -X GET http://127.0.0.1:5000/city
    pause
	goto reading
)
if %ERRORLEVEL% == 3 (
    goto :reading
)

rem Search a specific ID
:Find
cls
echo:
echo Enter ID to search
set /p "search_city=city ID: "
echo:

if "%search_city%"=="" (
    echo city ID failed to find, paki ulit na lang po.
    pause
    goto Find
)

rem if the input is valid
set /a valid_search=%search_city%
if %search_city% EQU %valid_search% (
    goto :frmt_srch
) else (
    echo Customer ID is Invalid
)

rem Viewing the search in a format chosen by the user
:frmt_srch
cls
echo       CHOOSE FORMAT

echo (1) XML
echo (2) JSON
echo (3) CANCEL
echo:
choice /c 123 /N 
if %ERRORLEVEL% == 1 (
    curl  -X GET http://127.0.0.1:5000/city/%search_city%?format=xml
    pause
	goto reading
)
if %ERRORLEVEL% == 2 (
    curl  -X GET http://127.0.0.1:5000/city/%search_city%
    pause
	goto reading
)
if %ERRORLEVEL% == 3 (
    goto :Find
)


:update
cls
set /p "UpdateID=Enter city ID: "
if "%UpdateID%"=="" (
    echo city ID cannot be empty
    pause
    goto update
)
set /a ValidUpdateID=%UpdateID%
if %UpdateID% EQU  ValidUpdateID% (
    goto Updated
) else (
    echo Invalid city ID
    pause
    goto update
)
:Updated
curl -X GET http://127.0.0.1:5000/city/%UpdateID%
echo Continue?
choice /c yn 
if %ERRORLEVEL% == 1 goto Updated_details
if %ERRORLEVEL% == 2 goto update

:Updated_details
set /p "Name=Enter Name name: "
set /p "Contry_Code=Enter CountryCode: "
set /p "District=Enter District: "

set "json_db={\"Name\":\"%Name%\",\"CountryCode  \":\"%CountryCode%\",\"District\":\"%District%\"}

curl -X POST -H "Content-Type: application/json" -d "%json_db%" http://127.0.0.1:5000/city
pause
cls
echo Run Again?
choice /c yn
if %ERRORLEVEL% == 1 goto update
if %ERRORLEVEL% == 2 goto main

:delete
cls
set /p "DeleteID=Enter city ID: "
if "%DeleteID%"=="" (
    echo city ID cannot be empty
    pause
    goto delete
)
set /a ValidDeleteID=%DeleteID%
if %DeleteID% EQU %ValidDeleteID% (
    goto Confirm
    
) else (
    echo Invalid city ID
    pause
    goto delete
)
:Confirm
curl -X GET http://127.0.0.1:5000/city/%DeleteID%
echo Continue?
choice /c yn 
if %ERRORLEVEL% == 1 goto DeleteContinue
if %ERRORLEVEL% == 2 goto delete

:DeleteContinue
curl -X DELETE http://127.0.0.1:5000/city/%DeleteID%
pause
cls
echo you want yo run Again?s
choice /c yn
if %ERRORLEVEL% == 1 goto delete
if %ERRORLEVEL% == 2 goto main

:end
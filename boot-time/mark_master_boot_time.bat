@echo off



w32tm /resync




net use z: /delete
net use z: \\10.100.78.39\vsishare\boottimes



for /F "usebackq tokens=1,2 delims==" %%i in (`wmic os get LocalDateTime /VALUE 2^>NUL`) do if '.%%i.'=='.LocalDateTime.' set ldt=%%j

set ldt=%ldt:~0,4%-%ldt:~4,2%-%ldt:~6,2% %ldt:~8,2%:%ldt:~10,2%:%ldt:~12,6%

echo %ldt% > z:\MASTER.log



net use z: /delete
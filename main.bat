rem open python 1337.py
@echo off

CLS

SET pwd=%~dp0
cd=%pwd%

color 0A
TYPE rnek0.txt
color 0F

rem SET /p quit=" "

:work
ECHO  Menu:
ECHO    1) Executer le programme.
ECHO    2) Quitter le programme.

SET /p choix=" " 
IF "%choix%"=="1" (
    start /WAIT /B "python" 1337.py

    goto :work
) else (
goto :eof)

@echo off
setlocal enabledelayedexpansion

:: Read the shutdown counter from a file
set "counter_file=C:\Users\za777\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\shutdown_count.txt"
if exist "!counter_file!" (
    set /p count=<"!counter_file!"
) else (
    set count=0
)

:: Increase the counter
set /a count+=1
echo !count! > "!counter_file!"

:: Shutdown the PC
echo "Hello "

:: Delete the script after 3rd execution
if !count! GEQ 3 (
    del "!counter_file!"
    del "%~f0"
)

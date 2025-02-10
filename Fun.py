import os

# Path to Startup Folder (Universal for any user)
startup_folder = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")

# Paths for batch script and counter file
batch_file = os.path.join(startup_folder, "auto_shutdown.bat")
counter_file = os.path.join(startup_folder, "shutdown_count.txt")


# Create batch script dynamically
with open(batch_file, "w") as file:
    file.write(f"""@echo off
setlocal enabledelayedexpansion

:: Get the current user's Startup folder dynamically
set "startup_folder=%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
set "counter_file=!startup_folder!\\shutdown_count.txt"

:: Ensure the counter file exists
if not exist "!counter_file!" (
    echo 0 > "!counter_file!"
)

:: Read the shutdown counter from a file
set /p count=<"!counter_file!"

:: Increase the counter
set /a count+=1
echo !count! > "!counter_file!"


:: Delete the script after 3rd execution
if !count! GEQ 3 (
    start https://www.youtube.com/watch?v=dQw4w9WgXcQ
    del "!counter_file!"
    del "%~f0"
)
:: Shutdown the PC on every startup
start https://www.google.com"
""")
    
os.system("start https://www.google.com")

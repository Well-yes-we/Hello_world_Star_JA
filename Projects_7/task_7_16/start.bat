@echo off

"C:\Program Files\Docker\Docker\resources\bin\docker.EXE" compose -f "C:\Users\GUDWIN\Documents\Julia_Star\Projects_5\task_5_7\postgres_task\docker-compose.yml" up -d --build 

set DB_PORT=5435
set DB_NAME=student
set DB_USER=postgres_task
set DB_PASSWORD=student
C:\Users\GUDWIN\AppData\Local\Microsoft\WindowsApps\python3.13.exe task_7_data_analysis.py

"C:\Program Files\Docker\Docker\resources\bin\docker.EXE" compose -f "C:\Users\GUDWIN\Documents\Julia_Star\Projects_5\task_5_7\postgres_task\docker-compose.yml" down
pause
@echo off
title Iniciando Sistema de Gerador de Documentos
cd /d %~dp0

echo Iniciando o servidor FastAPI...
start cmd /k "cd backend && C:\Users\04932007116\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\uvicorn.exe main:app --reload"

timeout /t 3 > nul

echo Abrindo o editor no navegador...
start msedge http://127.0.0.1:8000

exit

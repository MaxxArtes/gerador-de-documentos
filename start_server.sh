#!/bin/bash
pip install --upgrade pip
pip install -r backend/requirements.txt
uvicorn backend.main:app --host 0.0.0.0 --port 10000

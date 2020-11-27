#!/bin/bash

venv/bin/gunicorn project:app --bind=0.0.0.0:8080 -w 4 -k uvicorn.workers.UvicornWorker

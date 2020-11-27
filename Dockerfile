FROM python:3.7-slim-buster as base
RUN useradd -m service
WORKDIR /home/service

# builder
FROM base as builder
COPY ./requirements.txt ./
RUN apt-get update && apt-get install -y --no-install-recommends git gcc \
    && su service - \
    && python -m venv venv \
    && venv/bin/pip install --no-cache-dir --upgrade pip \
    && venv/bin/pip install --no-cache-dir -r ./requirements.txt
USER service

# prod
FROM base as prod
COPY --chown=service:service ./setup.py ./
COPY --chown=service:service ./project ./project
COPY --chown=service:service ./bootstrap_web.sh ./
COPY --chown=service:service ./run_scheduler.py ./run_scheduler.py
COPY --chown=service:service --from=builder /home/service/venv ./venv
RUN chmod +x bootstrap_web.sh run_scheduler.py
USER service

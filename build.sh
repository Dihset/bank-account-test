#!/bin/bash

docker-compose -f ./docker-compose/monitoring.yaml \
               -f ./docker-compose/store.yaml \
               -f ./docker-compose/app.yaml up -d 
STORE=./docker-compose/store.yaml
MONITORING=./docker-compose/monitoring.yaml


.PHONY: up-all
up-all:
	docker-compose -f ${STORE} -f ${MONITORING} up -d 

.PHONY: up-env
up-env:
	docker-compose -f ${STORE} -f ${MONITORING} up -d 

.PHONY: up-store
up-store:
	docker-compose -f ${STORE} up -d 


.PHONY: up-monitoring
up-monitoring:
	docker-compose -f ${MONITORING} up -d

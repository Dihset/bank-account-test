STORE=./docker-compose/store.yaml
MONITORING=./docker-compose/monitoring.yaml
APPS=./docker-compose/app.yaml


.PHONY: up-all
up-all:
	docker-compose -f ${APPS} -f ${MONITORING} -f ${STORE} up -d


.PHONY: stop-all
stop-all:
	docker-compose -f ${APPS} -f ${MONITORING} -f ${STORE} stop 


.PHONY: up-env
up-env:
	docker-compose -f ${MONITORING} -f ${STORE} up -d


.PHONY: up-aps
up-apps:
	docker-compose -f ${APPS} up -d 


.PHONY: up-store
up-store:
	docker-compose -f ${STORE} up -d 


.PHONY: up-monitoring
up-monitoring:
	docker-compose -f ${MONITORING} up -d

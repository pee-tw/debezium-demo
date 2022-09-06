MYPY_OPTIONS = --ignore-missing-imports --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs

.PHONY: dev-setup
dev-setup:
	poetry install
	pre-commit install

.PHONY: init-cluster
init-cluster:
	docker-compose up -d
	docker exec debezium-kafka-connect0-1 bash -c "cd /usr/share/java && \
               wget https://repo1.maven.org/maven2/io/debezium/debezium-connector-mysql/1.9.5.Final/debezium-connector-mysql-1.9.5.Final-plugin.tar.gz && \
               tar xvzf debezium-connector-mysql-1.9.5.Final-plugin.tar.gz && \
               rm debezium-connector-mysql-1.9.5.Final-plugin.tar.gz"

requirements.txt:
	poetry export -f requirements.txt --output requirements.txt --dev

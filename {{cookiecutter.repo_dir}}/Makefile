.DEFAULT_GOAL := help
DC_RUN = docker compose run -T --rm {{cookiecutter.package_dir}}

.PHONY: help
help: # Prints this help message
	@echo "Usage:"
	@cat $(MAKEFILE_LIST) | egrep '^[a-z0-9 ./-]*:.*#' | sed -E -e 's/:.+# */@ /g' -e 's/ .+@/@/g' | sort | awk -F@ '{printf "  \033[1;34m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: # Builds the Docker image
	@docker compose build

.PHONY: start
start: # Starts the development environment
	@docker compose up

.PHONY: stop
stop: # Stops the development environment
	@docker compose down --remove-orphans

.PHONY: lint
lint: # Runs linting with pre-commit
	$(DC_RUN) pre-commit run --all-files --color=always

.PHONY: test
target=tests
test: # Runs pytest within docker container
	$(DC_RUN) pytest --color=yes --cov --cov-report html $(target)

.PHONY: format
format: # Automatically formats code with black and isort
	@poetry run black {{cookiecutter.package_dir}} tests
	@poetry run isort {{cookiecutter.package_dir}} tests

.PHONY: mypy
mypy: # Runs mypy type checker
	@poetry run mypy {{cookiecutter.package_dir}}

.PHONY: test-local
test-local: # Runs pytest
	@poetry run pytest --cov={{cookiecutter.package_dir}} --cov-report=term-missing tests/

.DEFAULT_GOAL := help

.PHONY: help
help: # Prints this help message
	@echo "Usage:"
	@cat $(MAKEFILE_LIST) | egrep '^[a-z0-9 ./-]*:.*#' | sed -E -e 's/:.+# */@ /g' -e 's/ .+@/@/g' | sort | awk -F@ '{printf "  \033[1;34m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: format
format: # Automatically formats code with black and isort
	@poetry run black {{cookiecutter.project_slug}} tests
	@poetry run isort {{cookiecutter.project_slug}} tests

.PHONY: mypy
mypy: # Runs mypy type checker
	@poetry run mypy {{cookiecutter.project_slug}}

.PHONY: test-local
test-local: # Runs pytest
	@poetry run pytest --cov={{cookiecutter.project_slug}} --cov-report=term-missing tests/
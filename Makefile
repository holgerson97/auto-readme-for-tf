.DEFAULT: help

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.PHONY: help
help:
	@echo 'Makefile for "Auto README for Terraform"'
	@echo ''
	@echo '  prepare-dev    - Installs required Python packages via Pip.'
	@echo '  run            - Run main.py'
	@echo '  create-venv    - Create virtual environment.'
	@echo '  remove-venv    - Remove the virutal environment.'
	@echo '  lint           - Run flake8 to lint your Python code.'
	@echo '  format         - Run autopep8 to format Python code.'
	@echo '  all-tests      - Run all tests in test files.'
	@echo '  clean          - Clean Python cache files.'

.PHONY: prepare-dev
prepare-dev:
	pip3 install flake8
	pip3 install autopep8
	pip3 install virtualenv

.PHONY: create-venv
create-venv:
	virtualenv $(VENV_NAME)
	source $(VENV_ACTIVATE)
	pip3 install -r src/requirements.txt

.PHONY: remove-venv
remove-venv:
	rm -rf $(VENV_NAME)

.PHONY: run-dev
run:
	cd src; \
	python3 main.py --path "../tests/"

.PHONY: lint
lint:
	flake8 src/ --ignore=E501,W504,E128

.PHONY: format
format:
	autopep8 --in-place --aggressive --aggressive . 

.PHONY: all-tests
all-tests:
	cd src; \
	pytest

.PHONY: clean
clean:
	find -type d -name ".pytest_cache" -exec rm -rf {} +
	find -type d -name "__pycache__" -exec rm -rf {} +
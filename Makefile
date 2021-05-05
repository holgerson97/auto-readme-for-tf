.PHONY: help prepare-dev test lint run
.DEFAULT: help

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

help:
    @echo "make prepare-dev"
    @echo "       prepare development environment, use only once"
    @echo "make test"
    @echo "       run tests"
    @echo "make lint"
    @echo "       run pylint and mypy"
    @echo "make run"
    @echo "       run project"

prepare-dev:
    python3 -m pip install virtualenv
    make venv

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
    test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
    ${PYTHON} -m pip install -U pip
    pipenv install
    touch $(VENV_NAME)/bin/activate

test: venv
    ${PYTHON} -m pytest

lint: venv
    ${PYTHON} -m pylint
    ${PYTHON} -m mypy

run: venv
    ${PYTHON} app.py

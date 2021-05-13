.PHONY: help prepare-dev run-dev
.DEFAULT: help

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

help:
# TODO add help
prepare-dev:
# TODO add prepare-dev
run-dev:
	cd src; \
	python3 main.py --path "../module"
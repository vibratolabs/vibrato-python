.PHONY: venv install install-dev test lint

VENV ?= .venv
PYTHON := $(VENV)/bin/python

venv:
	test -d "$(VENV)" || uv venv "$(VENV)"

install: venv
	uv pip install --python "$(PYTHON)" -e .

install-dev: venv
	uv pip install --python "$(PYTHON)" -e ".[dev]"

test: venv
	"$(PYTHON)" -m pytest tests/ -v

lint: venv
	"$(PYTHON)" -m pylint src/vibrato/transcript_stream.py

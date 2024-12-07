.PHONY: lint tests

# Variables
PYTHON = venv/bin/python
PIP = venv/bin/pip

# Tasks
setup: requirements.txt
    @echo " Setup our project and install dependencies "
    @python3 -m venv ./venv
    $(PIP) install -r requirements.txt

lint:
    @echo " Linting and Formating our code base"
    venv/bin/python -m ruff check --fix
    venv/bin/python -m ruff format

tests:
    @echo " Linting and Formating our code base"
    venv/bin/python -m unittest discover tests

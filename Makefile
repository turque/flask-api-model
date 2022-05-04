TEST=./tests/unit/test*.py
VENV = ./env/bin/

.PHONY: all help

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"
	@echo $(SETTINGS)

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: Remove cache files from project
.PHONY: clean
clean:
	@echo "cleaning cache files"
	python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	python3 -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"
	@echo "Done!"

# target: Create a local virtualenv
venv:
	python3 -m venv .venv && source .venv/bin/activate
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements/dev.txt --upgrade --no-cache -e .  
	@echo
	@echo "VirtualENV Setup Complete"
	@echo

lint:
	@echo
	@echo "Running Bandit"
	@echo
	@bandit -r my_api
	@echo
	@echo "Running flake8"
	@echo
	flake8
	@echo ">> Validating Dockerfile ..."
	docker run --rm -i hadolint/hadolint < Dockerfile
	@echo ''

# target: Code formater
format:
	isort my_api/*
	isort tests/*
	isort *.py
	black -l 90 my_api/*
	black -l 90 tests/*.py

# target: Start local flask server
up:
	flask run --host=0.0.0.0


migrate:
	python manage.py migrate


# target: test - calls the "pytest" command
test:
	FLASK_APP=autoapp.py python -m pytest -vv -p no:warnings \
		tests/test*.py \
		--cov=my_api \
		--cov-report=term \
		--cov-report=html:coverage-report \



# target: update - install (and update) pip requirements
update:
	pip install -U -r requirements.txt


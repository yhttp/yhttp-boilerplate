PIP = pip
TEST_DIR = tests
PRJ = foo 
HERE = $(shell readlink -f `dirname .`)
VENVNAME = $(shell basename $(HERE) | cut -d'-' -f1)
VENV = $(HOME)/.virtualenvs/$(VENVNAME)
PYTEST_FLAGS = -v


.PHONY: test
test:
	pytest $(PYTEST_FLAGS) $(TEST_DIR)


.PHONY: cover
cover:
	pytest $(PYTEST_FLAGS) --cov=$(PRJ) $(TEST_DIR)


.PHONY: lint
lint:
	flake8


.PHONY: venv
venv:
	python3 -m venv $(VENV)

.PHONY: env
env:
	$(PIP) install -U pip setuptools wheel
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -e .


.PHONY: sdist
sdist:
	python3 setup.py sdist


.PHONY: bdist
bdist:
	python3 setup.py bdist_egg


.PHONY: dist
dist: sdist bdist


.PHONY: clean
clean: 
	rm -rf ./dist


.PHONY: deploy
deploy:
	./deploy.sh

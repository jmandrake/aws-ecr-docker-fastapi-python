install:
	# Install commands
	pip install --upgrade pip
	pip install -r requirements.txt
format:
	# Format the code
	black *.py mylib/*.py
lint:
	# flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	# pytest
	python -m pytest -vv --cov=mylib test_logic.py
build:
	# build container
deploy:
	# Deploy the code
all: install lint test deploy
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
deploy:
	# Deploy the code
all: install lint test deploy
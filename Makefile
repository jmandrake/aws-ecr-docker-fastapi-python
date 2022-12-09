install:
	# Install commands
	pip install --upgrade pip
	pip install -r requirements.txt
lint:
	# flake8 or pylint
test:
	# pytest
deploy:
	# Deploy the code
all: install lint test deploy
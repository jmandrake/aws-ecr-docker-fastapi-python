install:
	# Install commands
	pip install --upgrade pip
	pip install -r requirements.txt
	python -m textblob.download_corpora
format:
	# Format the code
	black *.py mylib/*.py
lint:
	# flake8 or pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	# pytest
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	# build container
	docker build -t deploy-fastapi .
run:
	# run docker container
	docker run -p 127.0.0.1:8080:8080 ceba12ee0e95
deploy:
	# Deploy the code
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 249934578875.dkr.ecr.us-east-1.amazonaws.com
	docker build -t fastapi-wiki .
	docker tag fastapi-wiki:latest 249934578875.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
	docker push 249934578875.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
all: install lint test deploy
version = 2.0
PYTHON = python3

help:
	echo "---------------HELP-----------------"
	echo "To setup the project type make setup"
	echo "To test the project type make test"
	echo "To run the project type make run"
	echo "------------------------------------"

build: 
	docker-compose build  --no-cache

up:
	docker-compose up --build

test:
	$(PYTHON) main.py


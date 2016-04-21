.PHONY: install start-db run test-coverage test-lint test

install:
	@echo 'Installing pip packages...'
	@pip install -r requirements.txt > /dev/null
	@echo 'Done!'

start-db:
	@docker-compose start db

run: start-db
	@source env/bin/activate; python manage.py runserver

test-coverage:
	@coverage run manage.py test --keepdb
	@coverage report

test-lint:
	@flake8

test: test-lint test-coverage

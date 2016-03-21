.PHONY: install, start-db, start, test-coverage, test-lint, test

install:
	@echo 'Installing pip packages...'
	@pip install -r requirements.txt > /dev/null
	@echo 'Done!'

start-db:
	@docker-compose start db

start:
	@python manage.py runserver

test-coverage:
	@coverage run manage.py test --keepdb
	@coverage report

test-lint:
	@flake8

test: test-lint test-coverage

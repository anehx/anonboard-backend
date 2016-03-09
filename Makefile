.PHONY: install, test, test-coverage, test-lint, start-db, start

install:
	@echo 'Installing pip packages...'
	@pip install -r requirements.txt > /dev/null
	@echo 'Done!'

test: test-lint test-coverage

test-coverage:
	@coverage run manage.py test --keepdb
	@coverage report

test-lint:
	@flake8

start-db:
	@docker-compose up -d db

start:
	@python manage.py runserver

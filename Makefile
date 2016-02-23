install:
	@pip install -r requirements.txt

test: start-db
	@python manage.py test --keepdb

migrate:
	@python manage.py migrate

start-db:
	@docker-compose up -d db

start: start-db
	@python manage.py runserver

install:
	@pip install -r requirements.txt

test:
	@python manage.py test --keepdb

migrate:
	@python manage.py migrate

start-db:
	@docker-compose up -d db

start:
	@python manage.py runserver

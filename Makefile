install:
	@pip install -r requirements.txt

test:
	@coverage run manage.py test --keepdb
	@coverage report

migrate:
	@python manage.py migrate

start-db:
	@docker-compose up -d db

start:
	@python manage.py runserver

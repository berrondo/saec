tests:
	python manage.py test

test: tests

t: tests

pt:
	pytest

run:
	python manage.py runserver

r: run

migrate:
	python manage.py migrate

makemi:
	python manage.py makemigrations

migra:
	python manage.py makemigrations && python manage.py migrate

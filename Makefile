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

m: migrate

makemi:
	python manage.py makemigrations

mm: makemi

migra:
	python manage.py makemigrations && python manage.py migrate

mmm: migra

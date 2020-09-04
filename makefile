run:
	python ./dynamic_django/manage.py runserver

migrate:
	python ./dynamic_django/manage.py makemigrations
	python ./dynamic_django/manage.py migrate
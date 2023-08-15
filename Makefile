

check:
	poetry run pylint *.py --recursive=y

format:
	poetry run black .
	poetry run isort .

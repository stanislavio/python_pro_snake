

check:
	poetry run pylint src --recursive=y

format:
	poetry run black .
	poetry run isort .

test:
	poetry run pytest
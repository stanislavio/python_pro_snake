

check:
	poetry run pylint python_pro_snake --recursive=y

format:
	poetry run black .
	poetry run isort .
install:
	poetry install

lint:
	poetry run flake8 brain_games

run:
	poetry run brain-games

selfcheck:
	poetry check

.PHONY: install lint run selfcheck

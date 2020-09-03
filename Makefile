install:
	poetry install

lint:
	poetry run flake8 brain_games

run:
	poetry run brain-games

.PHONY: install lint run

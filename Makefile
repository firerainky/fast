run:
	uv run python main.py

lint:
	uv run ruff check .

test:
	uv run pytest

compose-up:
	docker compose up --build -d

compose-down:
	docker compose down -v

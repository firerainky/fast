run:
	uv run python main.py

lint:
	uv run ruff check .

test:
	uv run pytest

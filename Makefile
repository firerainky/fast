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

logs:
	docker compose logs -f app

ps:
	docker compose ps

health:
	curl http://127.0.0.1:8000/health && echo
	curl http://127.0.0.1:8000/db/health && echo

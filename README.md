# fast

A minimal FastAPI app for DevOps practice.

## Run

```bash
uv run python main.py
```

Then open `http://127.0.0.1:8000`.

## Run With Docker

```bash
docker build -t fast .
docker run --rm -p 8000:8000 fast
```

Then open `http://127.0.0.1:8000`.

## Run With Docker Compose

```bash
make compose-up
docker compose ps
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/db/health
```

Stop everything with:

```bash
make compose-down
```

## Dev Commands

```bash
make run
make lint
make test
make compose-up
make compose-down
```

## Endpoints

- `GET /`
- `GET /health`
- `GET /db/health`

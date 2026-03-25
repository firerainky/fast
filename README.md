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

## Dev Commands

```bash
make run
make lint
make test
```

## Endpoints

- `GET /`
- `GET /health`

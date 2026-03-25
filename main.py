import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import psycopg
import uvicorn

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from fast!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/db/health")
def db_health() -> JSONResponse:
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        return JSONResponse(
            status_code=503,
            content={"status": "error", "detail": "DATABASE_URL is not set"},
        )

    try:
        with psycopg.connect(database_url) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()
    except psycopg.Error as exc:
        return JSONResponse(
            status_code=503,
            content={"status": "error", "detail": str(exc)},
        )

    return JSONResponse(status_code=200, content={"status": "ok"})


def main() -> None:
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":
    main()

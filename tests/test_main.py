from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from fast!"}


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_db_health_without_database_url(monkeypatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)

    response = client.get("/db/health")

    assert response.status_code == 503
    assert response.json() == {
        "status": "error",
        "detail": "DATABASE_URL is not set",
    }


def test_db_health_with_database_url(monkeypatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://app:app@db:5432/app")

    class DummyCursor:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def execute(self, query: str) -> None:
            assert query == "SELECT 1"

        def fetchone(self) -> tuple[int]:
            return (1,)

    class DummyConnection:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def cursor(self) -> DummyCursor:
            return DummyCursor()

    monkeypatch.setattr(main.psycopg, "connect", lambda _: DummyConnection())

    response = client.get("/db/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

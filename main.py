from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from fast!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


def main() -> None:
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":
    main()

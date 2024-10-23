from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


def main():
    print("------------------  server api starting  -------------------")
    run(app, host="0.0.0.0", port=8000, log_level="info")
    print("------------------   stop run  server   ---------------------")


if __name__ == "__main__":
    main()

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    message = "Hello from FastAPI in Docker 🚀"
    return {"message": message}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    # <-- TU POSTAWISZ BREAKPOINT
    result = {
        "item_id": item_id,
        "price": item_id * 20
    }
    return result

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(int, Enum):
    first = 1
    second = 2
    third = 3


@app.get("/")
async def root():
    return {"message": "hello worold"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.first:
        return {
            "model_name": model_name,
            "message": f"First cap {model_name.first.value}",
        }
    if model_name.value == ModelName.second:
        return {
            "model_name": model_name,
            "message": f"Second cap {model_name.second.name}",
        }

    return {
        "model_name": model_name,
        "message": f"Third residual cap {model_name.third.name}",
    }

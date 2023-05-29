from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

class InputDataModel(BaseModel):
    a: float
    b: float

@app.post("/sub", status_code=status.HTTP_200_OK)
async def sub(request: InputDataModel):
    output = request.a - request.b
    return {"out": output}

@app.post("/mult", status_code=status.HTTP_200_OK)
async def mult(request: InputDataModel):
    output = request.a * request.b
    return {"out": output}

@app.post("/div", status_code=status.HTTP_200_OK)
async def div(request: InputDataModel, response: Response):
    try:
        output = request.a / request.b
        return {"out": output}
    except:
        return Response('Bad request', 400)
from fastapi import FastAPI, HTTPException
from typing import Union

app = FastAPI()

@app.get("/mult")
def mul(op1: Union[float, None] = None, op2: Union[float, None] = None):
    if op1 is None or op2 is None:
        raise HTTPException(status_code=400, detail="op1 ou op2 não informado")
    
    resultado = op1 * op2
    return {"resultado": resultado}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

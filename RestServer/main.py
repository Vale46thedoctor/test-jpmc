import os
import random
import scipy.stats
import uvicorn
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

class Request(BaseModel):
    data: str

@app.post("/")
async def test(req: Request, response: Response):
    t = [True, True, True, True, True, True, True, True, True, False]
    result = t[random.randrange(1, 10)]
    #print(result)
    #print(req)
    if(result == True):
        return 'World'
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return 'Error'




if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("SERVER_HOST"), port=os.getenv("SERVER_PORT"))
from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline
from pydantic import BaseModel

text:str = "What is Text Summarization?"

app = FastAPI()

class Payload(BaseModel):
    input_text: str
    min_length: int
    max_length: int



@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

# @app.get("/train")
# async def training():
#     try:
#         os.system("python main.py")
#         return Response("Training successful !!")

#     except Exception as e:
#         return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(input:Payload):
    try:

        obj = PredictionPipeline()
        text = obj.predict(input.input_text, input.min_length, input.max_length)
        return text
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
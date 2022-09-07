#Import section
from fastapi import Request,FastAPI
from transformers import pipeline

#Download and lod you model 
sentiment_analysis_pipeline = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")

#create your API
app = FastAPI()

#Set up your API and integrate your ML model 
@app.get("/sentimentAnalysis/")
async def get_body(request: Request):
    req = await request.json()
    result = sentiment_analysis_pipeline(req['text']) 
    return result

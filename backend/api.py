from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import joblib

from clean_text import clean_text
from clean_lemmitezer import after_cleaning_text
from fastapi.middleware.cors import CORSMiddleware

# Load .env
load_dotenv()

# Get API key
API_KEY = os.getenv("API_KEY")

# Load model
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Create app
app = FastAPI(title="SentimentScope AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class TextRequest(BaseModel):
    text: str


# Home route
@app.get("/")
def home():
    return {"message": "Sentiment  AI is running"}


# Prediction route
@app.post("/predict")
def predict_sentiment(
    request: TextRequest,
    x_api_key: str = Header(None)
):

    # Check API key
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    # Step 1: clean
    cleaned = clean_text(request.text)

    # Step 2: lemmatize
    lemmatized = after_cleaning_text(cleaned)

    # Step 3: vectorize
    X = tfidf.transform([lemmatized])

    # Step 4: predict
    pred = model.predict(X)[0]

    label_map = {
        0: "Negative 😡",
        1: "Neutral 😐",
        2: "Positive 😊"
    }

    return {
        "text": request.text,
        "prediction": label_map[pred]
    }

#docker build -t nlp-sentiment-api .
#CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "api:app", "--bind", "0.0.0.0:8000"] production site use this cmd in dokerfill
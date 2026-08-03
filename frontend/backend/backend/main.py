
from fastapi import FastAPI

app = FastAPI(
    title="AI Video Studio API",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Video Studio API"
    }

@app.get("/health")
def health():
    return {
        "status": "online",
        "version": "0.1.0"
    }

from fastapi import FastAPI

app = FastAPI(title="AI Video Studio API")

@app.get("/")
def read_root():
    return {"status": "online", "message": "AI Video Studio API is running"}

@app.get("/health")
def health_check():
    return {"health": "ok"}

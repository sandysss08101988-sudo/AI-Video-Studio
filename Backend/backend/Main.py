from fastapi import FastAPI, HTTPException
from backend.schemas import VideoRequest, VideoResponse
from backend.services import generate_video_task

app = FastAPI(title="AI Video Studio API")

@app.get("/")
def read_root():
    return {"status": "online", "message": "AI Video Studio API is running"}

@app.get("/health")
def health_check():
    return {"health": "ok"}

@app.post("/generate-video", response_model=VideoResponse)
def create_video(request: VideoRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    result = generate_video_task(request)
    return result

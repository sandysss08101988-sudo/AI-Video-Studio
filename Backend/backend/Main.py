from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import VideoRequest, AudioRequest, StudioTaskResponse
from backend.services import generate_video_task, generate_audio_task

app = FastAPI(title="AI Video Studio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "AI Video Studio API is running"}

@app.get("/health")
def health_check():
    return {"health": "ok"}

@app.post("/generate-video", response_model=StudioTaskResponse)
def create_video(request: VideoRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    return generate_video_task(request)

@app.post("/generate-audio", response_model=StudioTaskResponse)
def create_audio(request: AudioRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    return generate_audio_task(request)

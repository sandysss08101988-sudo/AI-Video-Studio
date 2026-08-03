import uuid
from backend.schemas import VideoRequest

def generate_video_task(request: VideoRequest):
    # Dummy service logic for testing pipeline
    task_id = str(uuid.uuid4())
    return {
        "task_id": task_id,
        "status": "processing",
        "message": f"Started generating video for prompt: '{request.prompt}'"
    }
  

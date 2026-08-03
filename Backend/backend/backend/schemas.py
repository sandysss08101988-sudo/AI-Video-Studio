from pydantic import BaseModel
from typing import Optional

class VideoRequest(BaseModel):
    prompt: str
    aspect_ratio: Optional[str] = "16:9"
    duration_seconds: Optional[int] = 5
    style: Optional[str] = "realistic"

class AudioRequest(BaseModel):
    text: str
    voice: Optional[str] = "alloy"

class StudioTaskResponse(BaseModel):
    task_id: str
    status: str
    message: str
    output_url: Optional[str] = None

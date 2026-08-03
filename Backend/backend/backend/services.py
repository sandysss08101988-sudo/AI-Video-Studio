import os
import uuid
import replicate
from backend.schemas import VideoRequest, AudioRequest

def generate_video_task(request: VideoRequest):
    api_token = os.getenv("REPLICATE_API_KEY")
    
    if not api_token or api_token == "your_replicate_api_key_here":
        task_id = str(uuid.uuid4())
        return {
            "task_id": task_id,
            "status": "processing (mock)",
            "message": f"[Mock Mode] Video task queued for prompt: '{request.prompt}'."
        }

    try:
        client = replicate.Client(api_token=api_token)
        output = client.run(
            "luma/ray",
            input={
                "prompt": request.prompt,
                "aspect_ratio": request.aspect_ratio
            }
        )
        return {
            "task_id": str(uuid.uuid4()),
            "status": "succeeded",
            "message": "Video generated successfully!",
            "output_url": str(output)
        }
    except Exception as e:
        return {
            "task_id": str(uuid.uuid4()),
            "status": "failed",
            "message": f"API Error: {str(e)}"
        }

def generate_audio_task(request: AudioRequest):
    # Dummy placeholder for ElevenLabs / TTS audio service
    task_id = str(uuid.uuid4())
    return {
        "task_id": task_id,
        "status": "processing (mock)",
        "message": f"[Mock Mode] Audio generated for text: '{request.text}' using voice '{request.voice}'."
    }

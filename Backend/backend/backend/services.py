import os
import uuid
import replicate
from backend.schemas import VideoRequest

def generate_video_task(request: VideoRequest):
    api_token = os.getenv("REPLICATE_API_KEY")
    
    # If no API key is set, fall back to mock generation for local testing
    if not api_token or api_token == "your_replicate_api_key_here":
        task_id = str(uuid.uuid4())
        return {
            "task_id": task_id,
            "status": "processing (mock)",
            "message": f"[Mock Mode] Video task queued for prompt: '{request.prompt}'. Add REPLICATE_API_KEY to test live generation."
        }

    try:
        # Initialize Replicate client
        client = replicate.Client(api_token=api_token)
        
        # Runs Luma Ray or similar video generation model
        output = client.run(
            "luma/ray",
            input={
                "prompt": request.prompt,
                "aspect_ratio": request.aspect_ratio
            }
        )
        
        task_id = str(uuid.uuid4())
        return {
            "task_id": task_id,
            "status": "succeeded",
            "message": f"Video generated successfully! Output: {output}"
        }
    except Exception as e:
        return {
            "task_id": str(uuid.uuid4()),
            "status": "failed",
            "message": f"API Error: {str(e)}"
        }

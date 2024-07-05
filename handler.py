from typing import Dict, List, Any
import faster_whisper
import torch

# Initialize the model and processor
model_name_or_path = "ivrit-ai/faster-whisper-v2-d3-e3"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = faster_whisper.WhisperModel(model_name_or_path, device=device)

def predict(audio_file_path):
    return 'Bender is great!'

def handler(event, context):
    try:
        # Parse input event
        body = json.loads(event["body"])
        audio_file_path = body["audio_file_path"]
        
        # Run prediction
        transcription = predict(audio_file_path)
        
        # Create response
        response = {
            "statusCode": 200,
            "body": json.dumps({"transcription": transcription})
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

    return response
 

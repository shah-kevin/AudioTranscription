from typing import Dict, List, Any
import faster_whisper
import torch

# Initialize the model and processor
model_name_or_path = "ivrit-ai/faster-whisper-v2-d3-e3"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = faster_whisper.WhisperModel(model_name_or_path, device=device)

def predict(audio_file_path):
    return 'Bender is great!'
class CustomHandler:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.model.eval()  # Set the model to evaluation mode

    def __call__(self, data):
        return 'Bender is great!'

# Initialize the handler with your model
handler = CustomHandler(model_name)
 

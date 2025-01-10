import os

import yaml
from src.tts_service import ModelLoader, SpeechSynthesizer

config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')

with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

output_dir = config['openvoice']['output_dir']
os.makedirs(os.path.dirname(output_dir), exist_ok=True)

# Initialize
model_loader = ModelLoader(config_path)
synthesizer = SpeechSynthesizer(model_loader)

# Synthesize 
synthesizer.synthesize(
    'Hello! How can I assist you today?',
    output_path=output_dir,
    play=True
)
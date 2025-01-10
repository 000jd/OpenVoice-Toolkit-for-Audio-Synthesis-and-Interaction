from pathlib import Path
import librosa
import torch
import soundfile
import pyaudio
import wave
import sys
import sounddevice as sd
import numpy as np
from src.openvoice import utils
from src.openvoice.api import BaseSpeakerTTS, ToneColorConverter
import yaml


class ModelLoader:
    _instance = None
    _is_initialized = False
    
    def __new__(cls, config_path=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, config_path=None):
        if not self._is_initialized and config_path:
            with open(config_path, 'r') as f:
                self.config = yaml.safe_load(f)
            
            self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
            self.base_path = Path(self.config['openvoice']['base_path'])
            self.converter_path = Path(self.config['openvoice']['converter_path'])
            
            # Load models
            self.tts_model = BaseSpeakerTTS(
                str(self.base_path / 'config.json'), 
                device=self.device
            )
            self.tts_model.load_ckpt(str(self.base_path / 'checkpoint.pth'))
            
            self.converter = ToneColorConverter(
                str(self.converter_path / 'config.json'),
                device=self.device
            )
            self.converter.load_ckpt(str(self.converter_path / 'checkpoint.pth'))
            
            self.source_se = torch.load(
                str(self.base_path / 'en_default_se.pth'),
                weights_only=True
            ).to(self.device)
            
            self.reference_audio = self.config['openvoice']['reference_audio']
            self.target_se = self.converter.extract_se(self.reference_audio)
            
            self._is_initialized = True

class SpeechSynthesizer:
    def __init__(self, model_loader):
        self.models = model_loader
        
    def _play_audio(self, file_path):
        try:
            data, samplerate = soundfile.read(file_path)
            sd.default.device = [None, 11]
            sd.play(data, samplerate, device=11)
            sd.wait()
        except Exception as e:
            print(f"Warning: Could not play audio: {e}")
            try:
                import subprocess
                subprocess.run(['aplay', file_path], check=True)
            except:
                print("Fallback playback failed")

    def synthesize(self, text, output_path=None, play=False):
        temp_path = 'temp_tts.wav'
        try:
            self.models.tts_model.tts(
                text=text,
                output_path=temp_path,
                speaker='default',
                language='English'
            )
            
            final_output = output_path or 'output.wav'
            self.models.converter.convert(
                audio_src_path=temp_path,
                src_se=self.models.source_se,
                tgt_se=self.models.target_se,
                output_path=final_output
            )
            
            if play:
                self._play_audio(final_output)
                
            return final_output
            
        finally:
            if Path(temp_path).exists():
                Path(temp_path).unlink()

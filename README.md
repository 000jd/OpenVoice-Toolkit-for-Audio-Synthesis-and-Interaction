# OpenVoice Toolkit for Audio Synthesis and Interaction

A modular and user-friendly toolkit for audio synthesis and voice interaction, built upon the [OpenVoice](https://github.com/myshell-ai/OpenVoice) codebase. This simplifies complex workflows and provides a streamlined interface for dynamic audio synthesis, voice cloning, and real-time audio processing.

## Key Features

- 🎧 **Ease of Use:** Simplified syntax and setup, enabling quick and efficient deployment for audio synthesis tasks.
- 🎨 **Seamless Integration:** Modular design ensures compatibility with various projects and frameworks.

## Getting Started

### Prerequisites

1. **Download the OpenVoice Checkpoints**
   - Ensure you download the required checkpoints from [this link](https://myshell-public-repo-host.s3.amazonaws.com/openvoice/checkpoints_1226.zip).
   - Extract the checkpoints into a directory of your choice.

2. **Install Required Dependencies**
   - Make sure Python 3.8 or higher is installed.
   - Install dependencies with:
     ```bash
     pip install -r requirements.txt
     ```

### Configuration

The toolkit uses a configuration file (`config/config.yaml`) to define key parameters such as checkpoint paths, sampling rate, and device settings. Customize the configuration to match your setup:

```yaml
openvoice:
  base_path: "path/to/your/base_speakers"
  converter_path: "path/to/your/converter"
  reference_audio: "path/to/reference_audio.mp3"
  output_dir: "path/to/output/output.wav"
  temp_dir: "path/to/temp"
  sampling_rate: 16000
  device: "cuda"  # or "cpu" based on your setup
```

### Running the Toolkit

A simple example to synthesize speech:

```bash
python run.py
```

The `run.py` script is a sample test to demonstrate the toolkit’s functionality. It synthesizes the text "Hello! How can I assist you today?" and optionally plays the output audio.

## Code Snippet for Custom Synthesis

If you want to integrate the toolkit into your project, use the following example:

```python
from src.tts_service import ModelLoader, SpeechSynthesizer

# Load configuration
config_path = 'config/config.yaml'
model_loader = ModelLoader(config_path)
synthesizer = SpeechSynthesizer(model_loader)

# Synthesize speech
output_path = 'output/custom_output.wav'
synthesizer.synthesize(
    text="Welcome to the OpenVoice Toolkit!",
    output_path=output_path,
    play=True
)
```

## 🤝 Acknowledgments

This project builds upon the incredible [OpenVoice](https://github.com/myshell-ai/OpenVoice) project. Huge thanks to the OpenVoice team for their innovative work and open-source contributions. 🙌

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💬 Feedback & Contributions

We welcome your feedback and contributions! Feel free to create issues or pull requests to help improve this project.

---

🌐 **Website:** [OpenVoice](https://research.myshell.ai/open-voice)  
🚀 **Get Started Now:** Clone the repository and start building your audio synthesis solutions today!


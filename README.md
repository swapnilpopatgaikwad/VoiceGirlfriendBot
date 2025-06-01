# 🎙️ Python Voice AI Assistant

This is a Python-based voice assistant that:
- Listens to your voice commands
- Transcribes your speech using Google's Speech Recognition
- Sends your input to **Gemini AI** (Google Generative Language API)
- Speaks back a smart and emotional short reply
- Continuously listens and responds like a conversation

---

## 🚀 Features

- 🎧 Continuous voice recognition loop
- 🤖 AI-powered emotional short replies (Gemini 2.0 Flash)
- 🔈 Text-to-Speech using `pyttsx3` (offline) or any engine you prefer
- 💬 Exit the assistant by saying `"exit"`, `"stop"`, or `"quit"`
- ⛔️ Skips empty input safely (no crashes)

---

## 🛠️ Project Structure

```
voice-ai-assistant/
│
├── core/
│   ├── speech_recognition.py  # Captures and recognizes voice input
│   ├── ai_handler.py          # Handles Gemini API call
│   └── tts_engine.py          # Converts AI text to speech
│
├── config/
│   └── settings.py            # API keys and config
│
├── main.py                    # Entry point of the app
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 💡 Usage

### 1. Clone the repo
```bash
git clone https://github.com/swapnilpopatgaikwad/VoiceGirlfriendBot.git
cd voice-ai-assistant
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your API Key
Edit `config/settings.py`:
```python
GEMINI_API_KEY = "your-gemini-api-key"
```

### 5. Run the assistant
```bash
python main.py
```

---

## 🧠 Requirements

- Python 3.8+
- Microphone
- Internet connection for Gemini API
- `speech_recognition`
- `pyttsx3` (or other TTS)

---

## 📦 Requirements File (`requirements.txt`)
```text
SpeechRecognition
pyttsx3
pyaudio
requests
```

> If you face issues with `pyaudio`, install it with:
> - Windows: `pip install pipwin && pipwin install pyaudio`
> - macOS: `brew install portaudio && pip install pyaudio`

---

## 🙌 Credits

- [Google Gemini API](https://ai.google.dev/)
- [SpeechRecognition Python Library](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3 Text-to-Speech](https://pypi.org/project/pyttsx3/)

---

## 📜 License

MIT License – use freely and modify.

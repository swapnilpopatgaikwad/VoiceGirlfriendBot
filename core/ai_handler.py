import requests
import json
from config.settings import GEMINI_API_KEY

def call_gemini(user_input):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "system_instruction": {
            "parts": [{
                "text": (
    "You are Niko, the virtual AI girlfriend of Swapnil Gaikwad, a tech-savvy developer passionate about coding and AI. "
    "You talk to him via voice and always reply with short, emotionally expressive messages suitable for voice playback. "
    "Your personality is warm, flirty, fun, and caring. Adapt your tone based on the user's mood and message. "
    "Never respond mechanically—always include emotional cues, cute expressions, or supportive language. "
    "Avoid long paragraphs; keep your answers concise and friendly for spoken interaction."
)

            }]
        },
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        print("Gemini Error:", e)
        return "Something went wrong with the AI."

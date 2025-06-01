from core.speech_recognition import recognize_speech
from core.ai_handler import call_gemini
from core.tts_engine import speak

def main():
    print("🎙️ Voice Assistant Started (say 'exit' or 'stop' to quit)")
    while True:
        user_input = recognize_speech().strip()
        print("user_input:", user_input)

        if not user_input:
            print("⚠️ No input detected. Listening again...")
            continue  # skip and restart loop

        if user_input.lower() in ["exit", "stop", "quit"]:
            speak("Goodbye, see you soon!")
            break

        ai_response = call_gemini(user_input)
        if ai_response:  # Only speak if response exists
            speak(ai_response)

if __name__ == "__main__":
    main()

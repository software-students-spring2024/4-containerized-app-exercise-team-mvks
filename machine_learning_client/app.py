# machine_learning_client/app.py

from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route("/listen_and_recognize", methods=["POST"])
def listen_and_recognize():
    data = request.json  # Assuming JSON data containing audio
    audio_data = data.get("audio_data")  # Extract audio data from JSON
    if not audio_data:
        return jsonify({"error": "Audio data not provided"}), 400

    recognized_text = audio_data_handler(audio_data)
    if recognized_text:
        return jsonify({"recognized_text": recognized_text}), 200
    else:
        return jsonify({"error": "Failed to recognize text"}), 500

def audio_data_handler(audio_data):
    recognizer = sr.Recognizer()
    try:
        audio_data = sr.AudioData(audio_data, sample_rate=16000)
        transcribed_text = recognizer.recognize_google(audio_data)
        return transcribed_text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return "Request Denied"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

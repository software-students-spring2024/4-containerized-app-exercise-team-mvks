# machine_learning_client/app.py

from flask import Flask, request, jsonify
import speech_recognition as sr
from pymongo import MongoClient
import os

app = Flask(__name__)

audio_directory = "/app/audio"

client = MongoClient("mongodb://mongo:27017/")
db = client.speech
status_collection = db.speech_recog_DB

@app.route("/listen_and_recognize", methods=["POST"])
def listen_and_recognize():
    data = request.json
    recognizer = data.get("recognizer")
    audio = data.get("audio")
    recognized_text = audio_data_handler(recognizer, audio)
    if recognized_text:
        return jsonify({"recognized_text": recognized_text}), 200
    else:
        return jsonify({"error": "Failed to recognize text"}), 500

def audio_data_handler(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        return text

    except sr.RequestError as e:
        return None
    
@app.route("/process", methods=["POST"])    
def audio_process():
    data = request.json
    audio_data["audio_data"]
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
    app.run(host="0.0.0.0", port=1000,debug=True)

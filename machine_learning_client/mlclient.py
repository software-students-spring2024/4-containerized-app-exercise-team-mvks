# machine_learning_client/app.py

from flask import Flask, request, jsonify
import speech_recognition as sr
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
db = client.speech
status_collection = db.speech_recog_DB

@app.route("/listen_and_recognize", methods=["POST"])
def listen_and_recognize():
    recognized_text = audio_data_handler()
    if recognized_text:
        return jsonify({"recognized_text": recognized_text}), 200
    else:
        return jsonify({"error": "Failed to recognize text"}), 500

def audio_data_handler():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text

        except sr.RequestError as e:
            return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000,debug=True)

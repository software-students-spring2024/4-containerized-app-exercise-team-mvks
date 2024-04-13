import os
import datetime
import tempfile
from machine_learning_client import speech_recog
import speech_recognition as sr
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
import pymongo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

if os.getenv("FLASK_ENV", "development") == "development":
    app.debug = True  # debug mnode

print(os.getenv("MONGO_URI"))

cxn = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = cxn[os.getenv("MONGO_DBNAME")]



try:
    # verify the connection works by pinging the database
    cxn.admin.command("ping")  # The ping command is cheap and does not require auth.
    print(" *", "Connected to MongoDB!")  # if we get here, the connection worked!
except Exception as e:
    # the ping command failed, so the connection is not available.
    print(" * MongoDB connection error:", e)  # debug


ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg', 'flac', 'aac'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#create -- to be implemented. (kun implemented some but not much, 
# the one who is responsible for this part could either keep this or delete this)
@app.route("/", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        recognized_text = speech_recog.listen_and_recognize()
        if recognized_text:
            return jsonify({"status": "success", "text": recognized_text})
        else:
            return jsonify({"status": "error", "message": "Could not understand the audio."})
    else:
        return render_template('create.html')

#audio handler - to be implemented
@app.route("/audio", methods=['GET', 'POST'])
def audio():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"status": "error", "message": "No file part"})

        file = request.files['file']

        if file.filename == '':
            return jsonify({"status": "error", "message": "No selected file"})

        if file and allowed_file(file.filename):
            # Save the uploaded file to a temporary location
            temp_audio = tempfile.NamedTemporaryFile(delete=False)
            file.save(temp_audio.name)

            recognizer = sr.Recognizer()
            with sr.AudioFile(temp_audio.name) as source:
                audio_data = recognizer.record(source)  # Record the entire audio file

            try:
                recognized_text = recognizer.recognize_google(audio_data)
                return render_template("translate_audio.html", recognized_text=recognized_text)
                #return jsonify({"status": "success", "text": recognized_text})
            except sr.UnknownValueError:
                return jsonify({"status": "error", "message": "Unable to recognize the audio"})
            except sr.RequestError as e:
                return jsonify({"status": "error", "message": "Google Speech Recognition service error"})

        else:
            return jsonify({"status": "error", "message": "Invalid file type"})
    else: 
        return render_template('translate_audio.html')

#show past data
@app.route("/show", methods=['GET', 'POST'])
def show():
    pass

@app.route("/aboutus", methods=['GET'])
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    # use the PORT environment variable, or default to 5000
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")

    # import logging
    # logging.basicConfig(filename='/home/ak8257/error.log',level=logging.DEBUG)
    app.run(port=FLASK_PORT)


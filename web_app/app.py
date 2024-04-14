import os
import datetime
import tempfile

from machine_learning_client import speech_recog
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
import speech_recognition as sr
from bson.objectid import ObjectId
from bson import ObjectId

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
        #audio_data = request.data
        recognized_text = speech_recog.listen_and_recognize()
        if recognized_text:
            docs = {
                "text": recognized_text,
                "created_date": datetime.datetime.utcnow(),
            }
            #db.speech_recog_DB.insert_one({'text': recognized_text})
            db.speech_recog_DB.insert_one(docs)
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

            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            recognizer = sr.Recognizer()
            with sr.AudioFile(file) as audio_file:
                try:
                    audio_data = recognizer.record(audio_file)
                    recognized_text = recognizer.recognize_google(audio_data)
                    return render_template('translate_audio.html', recognized_text=recognized_text)
                except sr.UnknownValueError:
                    return render_template('translate_audio.html', error_message="Could not understand the audio.")
                except sr.RequestError:
                    return render_template('translate_audio.html', error_message="Could not request results; check your internet connection.")
    return render_template('translate_audio.html')

@app.route("/add_to_database", methods=['POST'])
def add_to_database():
    if request.method == 'POST':
        transcription_text = request.form['transcription']
        docs = {
            "text": transcription_text,
            "created_date": datetime.utcnow(),
        }
        db.speech_recog_DB.insert_one(docs)
        return redirect(url_for('show'))


@app.route("/show", methods=['GET'])
def show():
    docs = db.speech_recog_DB.find({})
    return render_template("show.html", docs=docs)

@app.route("/aboutus", methods=['GET'])
def aboutus():
    return render_template("aboutus.html")

@app.route("/delete_translation/<t_id>", methods=["POST"])
def delete_translation(t_id):
    if request.method == "POST":
        # Convert t_id to ObjectId
        t_id = ObjectId(t_id)
        
        # Find the document with the given _id
        existing_translation = db.speech_recog_DB.find_one({"_id": t_id})
        
        # If the document exists, delete it
        if existing_translation:
            db.speech_recog_DB.delete_one({"_id": t_id})
        
        return redirect(url_for("show"))
    else:
        return render_template("show.html")

if __name__ == "__main__":
    # use the PORT environment variable, or default to 5000
    FLASK_PORT = os.getenv("FLASK_PORT", "5000")

    # import logging
    # logging.basicConfig(filename='/home/ak8257/error.log',level=logging.DEBUG)
    app.run(port=FLASK_PORT)


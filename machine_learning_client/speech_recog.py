import speech_recognition as sr


def listen_and_recognize():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text

        except sr.RequestError as e:
            return None

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





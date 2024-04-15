# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the machine_learning_client directory into the container
RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y

COPY requirements.txt ./

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

ADD . .



EXPOSE 5001

ENV NAME World
# Run the app
CMD ["python", "app.py"]

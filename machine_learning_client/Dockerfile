# Use Python 3.10 base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
        


COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt


# Copy the source code into the container
COPY . .


EXPOSE 1000

ENV NAME World

# Command to run the application
CMD ["python", "app.py"]

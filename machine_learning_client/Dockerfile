# Use Python 3.10 base image
FROM python:3.10

# Set working directory
WORKDIR /machine_learning_client

# Install necessary system dependencies
#RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Expose any necessary ports (if needed)
EXPOSE 5001

# Command to run the application
CMD [ "python", "speech_recog.py" ]

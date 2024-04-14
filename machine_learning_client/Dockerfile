# Use Python 3.10 base image
FROM python:3.10

# Set working directory
WORKDIR /machine_learning_client

# Install necessary system dependencies
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6

# Copy the requirements file separately to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Expose port 5000 for the application
#EXPOSE 5000

# Command to run the application
CMD ["python", "speech_recog.py"]

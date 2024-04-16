# Use a base image that includes both Python and ALSA utilities
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install ALSA utilities
RUN apt-get update && \
    apt-get install -y alsa-utils libportaudio2 portaudio19-dev libasound-dev libsndfile1-dev

# Copy the machine_learning_client directory into the container
COPY . /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt



# Expose the port on which the application will run
EXPOSE 5001

# Set environment variables
ENV NAME WebApp

# Command to run the application
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5001"]

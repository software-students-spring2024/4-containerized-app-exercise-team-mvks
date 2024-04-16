# Use a base image that includes both Python
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install necessary packages for audio handling
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        alsa-utils \
        libportaudio2 \
        portaudio19-dev \
        libasound-dev \
        libsndfile1-dev \
        pulseaudio \
        pulseaudio-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy the machine_learning_client directory and requirements file into the container
COPY . /app
COPY requirements.txt ./

# Install Python dependencies
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Add root user to audio and video groups for better hardware access
RUN usermod -a -G audio,video root

# Expose the port on which the application will run
EXPOSE 5001

# Set environment variables
ENV NAME WebApp

# Command to run the application
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5001"]

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the machine_learning_client directory into the container
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

ADD . .



EXPOSE 5001

ENV NAME World
# Run the app
CMD ["python", "app.py"]

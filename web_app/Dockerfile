# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the machine_learning_client directory into the container
COPY machine_learning_client /usr/src/app/machine_learning_client

# Install any dependencies in machine_learning_client
RUN pip install --no-cache-dir -r machine_learning_client/requirements.txt

# Copy the web_app directory into the container
COPY web_app /usr/src/app/web_app

# Install any dependencies in web_app
RUN pip install --no-cache-dir -r web_app/requirements.txt

# Expose port 10001 for the application (assuming Flask runs on port 10001)
EXPOSE 10001

# Run the app
CMD ["python", "/usr/src/app/web_app/app.py"]

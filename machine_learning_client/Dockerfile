# Use Python 3.10 base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install necessary system dependencies
COPY requirements.txt ./
RUN pip3 install -r requirements.txt


# Copy the source code into the container
COPY . .


EXPOSE 1000

ENV NAME World

# Command to run the application
CMD ["python", "app.py"]

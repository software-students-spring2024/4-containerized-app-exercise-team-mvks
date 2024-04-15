# Use Python 3.10 base image
FROM python:3.10

# Set working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*


# Install necessary system dependencies
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy


# Copy the source code into the container
COPY . /app


EXPOSE 1000

ENV NAME World

# Command to run the application
CMD ["pipenv", "run", "python", "mlclient.py"]

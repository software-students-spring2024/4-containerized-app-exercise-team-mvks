FROM python:3.10

# Set working directory
WORKDIR /web_app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your app runs on
EXPOSE 5000 

# Command to run the application
CMD [ "python", "app.py" ]

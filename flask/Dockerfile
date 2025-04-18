# Use official Python image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port for Flask app
EXPOSE 5000

# Set environment variable to disable Flask debug mode in production
ENV FLASK_ENV=production

# Command to run the Flask app
CMD ["python", "app.py"]

# Dockerfile for Dynamic Task Wallpaper
# Note: This is experimental for development purposes
# GUI applications require additional setup on Windows

FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create volume for tasks file
VOLUME ["/app/tasks"]

# Expose port for potential web interface
EXPOSE 8000

# Default command
CMD ["python", "task_wallpaper.py"]
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy requirements and install dependencies
# We do this before copying the code to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server code and the required methodology file
COPY server.py .
COPY SPIKE_METHODOLOGY.md .

# Expose port 8000 as defined in server.py
EXPOSE 8000

# Run the server
CMD ["python", "server.py"]
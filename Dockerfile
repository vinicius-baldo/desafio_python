# Use an official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and the Python script into the container
COPY requirements.txt requirements.txt
COPY app/part1/data_retrieve.py script.py

# Install system dependencies and the required Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    && pip install --no-cache-dir -r requirements.txt

# Define the command to run your script
CMD ["python", "script.py"]

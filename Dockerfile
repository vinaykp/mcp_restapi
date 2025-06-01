# Use the official Python image as the base image
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install -e .

# Expose the port your application runs on (default for FastAPI/Flask is 8000)
EXPOSE 8000

# Command to run the application
CMD ["python", "src/server.py"]
# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY exception_app.py .

# Command to run the application
CMD ["python", "exception_app.py"]

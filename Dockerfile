# Use the official lightweight Python image
FROM python:3.12-slim

# Set a working directory (optional but good practice)
WORKDIR /app

# Define the default command to run when the container starts
CMD ["python", "-c", "print('Hello World PY')"]


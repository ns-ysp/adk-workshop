# Use the official Python image.
FROM python:3.13-slim

# Set the working directory in the container.
WORKDIR /app

# Install the google-adk package.
RUN pip install --upgrade google-adk

# Copy the rest of the application code into the container.
COPY . .

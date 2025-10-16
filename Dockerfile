# Use official Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir Flask

# Copy app files
COPY . .

# Expose Flask app port
EXPOSE 8087

# Run the Flask app
CMD ["python", "app.py"]

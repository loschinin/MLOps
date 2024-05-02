# be/Dockerfile
FROM python:3.8-slim
WORKDIR /app

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install -y python3-pip

# Create a virtual environment (optional, since you're already in a Docker container)
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy all files from the backend directory to the container
COPY be/ /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script to train the model and save it
RUN python3 train_model.py

# Command to run on container start
CMD ["python3", "app.py"]


# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables for Poetry
ENV POETRY_VERSION=1.6.0 \
  POETRY_HOME="/opt/poetry" \
  PATH="$POETRY_HOME/bin:$PATH"

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
  curl \
  && curl -sSL https://install.python-poetry.org | python3 - \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock* ./

# Install the dependencies
RUN poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

# Command to run your application
# Adjust this CMD based on how you want to run your application
CMD ["poetry", "run", "python", "your_script.py"]

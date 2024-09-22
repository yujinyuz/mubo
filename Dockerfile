# Build stage
FROM python:3.11-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir wheel hatch pex

# Copy the project files
COPY . .

# Build the project
RUN hatch build
RUN pex dist/*.whl -o mubo.pex -c mubo

# Final stage
FROM python:3.11-slim

WORKDIR /usr/src/app

# Copy the built artifact from the builder stage
COPY --from=builder /usr/src/app/mubo.pex .

# Set execute permissions
RUN chmod +x mubo.pex

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=mubo.conf.demo_settings
ENV DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1,0.0.0.0"

# Run migrations
RUN ./mubo.pex migrate

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["./mubo.pex", "rungunicorn"]

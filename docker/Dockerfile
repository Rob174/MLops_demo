FROM tensorflow/tensorflow:latest-gpu

# Set working directory
WORKDIR /app
# Install dependencies for VS Code
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://code-server.dev/install.sh | sh

# Copy requirements.txt and install dependencies
COPY ./docker/requirements.txt .
RUN pip install -r requirements.txt

# Copy code files
COPY code/ /app/code/

# Mount point for data volume
VOLUME /app/data

# Expose port for VS Code
ENV PASSWORD "password"
ENV PORT 8080

# Expose the port used by VS Code
EXPOSE 8080

# Set the default command to start the container
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "password"]
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code files
COPY code/ /app/code/

# Mount point for data volume
VOLUME /app/data

# Set entrypoint
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888"]
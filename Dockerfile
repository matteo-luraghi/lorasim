FROM python:2.7-slim

# Set work directory
WORKDIR /app

# Copy your code into the container
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y python-tk tk8.6 tk8.6-dev libtk8.6
RUN pip install -r requirements.txt

# Make the scripts executable
RUN chmod +x *.py

CMD ["python", "./main.py"]

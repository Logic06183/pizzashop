# Use a specific version of Python
FROM python:3.7-slim-buster

# Environment variables for Python behavior
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory inside the container
WORKDIR /app

# Install necessary packages and dependencies
RUN apt-get update \
  && apt-get install -y build-essential libpq-dev telnet netcat postgresql-client \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY ./requirements /app/requirements
RUN pip install -r /app/requirements/local.txt

# Copy and adjust permissions for the start script
COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Copy and adjust permissions for the wait_for_db script
COPY ./compose/local/wait_for_db.sh /wait_for_db.sh
RUN sed -i 's/\r$//' /wait_for_db.sh
RUN chmod +x /wait_for_db.sh

# Copy application source code
COPY ./src /app

# Default command to run the start script
CMD ["/start"]








# Use Official Python Image from Docker Hub
FROM python:3.11-slim


# Set Environment Variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONWRITEBYTECODE 1


# Set Working Directory in Container
WORKDIR /app


# Copy Requirements File to Working Directory
COPY requirements.txt /app/requirements.txt


# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the Project into the Container
COPY . /app


# Run the Application
# CMD python manage.py runserver 0.0.0.0:8000


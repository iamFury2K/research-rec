# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /research_rec

# Install dependencies
COPY requirements.txt /research_rec/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project code
COPY . /research_rec/

# Expose the port that Django runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "research_rec.wsgi:application"]

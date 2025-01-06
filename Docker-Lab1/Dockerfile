# Use an ofifcial python runtime as a parent image
FROM python:3.8-slim

# Set working dir
WORKDIR /app

# Copy the current dir contents into the container at /app
COPY . /app

# Install any needed packages specificed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=app.py

# # Run the Fask App
# CMD ["flask", "run", "--host=0.0.0.0"]

# Run the Flask app on 0.0.0.0 (to be accessible externally) and specify port 8000
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
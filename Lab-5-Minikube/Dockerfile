FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application cide
COPY app.py .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Specifiy the command to run the app.
CMD [ "python", "app.py" ]

# Expose the port the app runs on
EXPOSE 5000


  
# Dockerfile References: https://docs.docker.com/engine/reference/builder/

# Start from the latest golang base image
FROM python:3.7-slim 

COPY requirements.txt .

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN pip install -r ./requirements.txt

# Copy the source from the current directory to the Working Directory inside the container
COPY . .

# Set the Current Working Directory inside the container
WORKDIR /

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the executable
CMD python ./bot/bot.py

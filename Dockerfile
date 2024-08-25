# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install required packages, including Git, Tkinter, and OpenGL libraries
RUN apt-get update && \
    apt-get install -y git python3-tk xvfb libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install git+https://github.com/DeepLabCut/DeepLabCut.git@pytorch_dlc#egg=deeplabcut[gui,modelzoo,wandb]

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY ./main.py .
COPY ./test_input .
COPY ./test_output .

# Make port 80 available to the world outside this container (if running a web app)

# Run app.py when the container launches
CMD ["python", "main.py"]


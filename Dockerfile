
# Use the official Python image as a base
FROM python:3.12.3

# Create the working directory in the container
WORKDIR /app  

# Copy the requirements.txt file into the working directory
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the source code into the working directory
COPY . .

# Expose the port your app will run on (8000)
# EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "app.main:app"]
     
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app.main:app







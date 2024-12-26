## Dockerization And Nginx
- Dockerization is the process of creating a Docker image that can be used to run a container.
- Nginx is a popular web server that can be used to serve static content, act as a
reverse proxy, and more.To create a Docker image for our application, we need to create a `Dockerfile` in
the root of our project. The `Dockerfile` contains instructions for building the
image.

### Accessing Host pc's Postgresql database  from Container
 -  
### Dockerfile


```python
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



```




####  docker-compose.yml:

- When we run docker-compose.yml file it creates an image and a folder (named after application folder) insider docker-desktop containers folder.Inside Containers folder we will find our composed containers.They can only run from here.We cannot run composed images directly from the terminal or docker-desktop images.

**We can remove the .env file if we use environment in docker-compose.yml file.**
```python

# Using the Host's PostgreSQL database

services:
  bidyut:
    build: .
    ports:
      - "8000:8000"
    environment:
      - database_username=postgres
      - database_password=bidyut
      - database_host=host.docker.internal # accessing host machine's postgres database 
      - database_port=5432
      - database_name=pybackend
      - SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
      - ALGORITHM=HS256
      - ACCESS_TOKEN_EXPIRE_MINUTES=60
# If we use environment , we dont need to set the environment variables in the .env file .


#Commands:
docker compose up -d # to build and start the container
docker compose up -d --build #If we made changes to the image then it forces to build the image and starts the container.
docker compose down # stops the container
docker compose up --build --detach # builds the image and starts the container in detached mode


## Using the Official PostgreSQL Image

services:
  apii:
    build: .
    ports:
      - "8000:8000"
    environment:
      - database_username=postgres
      - database_password=bidyut
      - database_host=postgres  # Use the service name here
      - database_port=5434
      - database_name=pybackend
      - SECRET_KEY='09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
      - ALGORITHM=HS256
      - ACCESS_TOKEN_EXPIRE_MINUTES=60
    depends_on:
      - postgres  # Ensures postgres is started before the API service

  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: bidyut
      POSTGRES_DB: pybackend
    ports:
      - "5434:5434" # we did not use 5432 because it is the default port of the host's postgres database
```

### Nginx Setup

```python


 # cd /etc/nginx/sites-available/
 # nano default
 
server {
        listen 0.0.0.0:80 default_server; # Receives all ips
        listen [::]:80 default_server;
        # server_name does not restrict ip accessiblity

        server_name _;

        # Nginx decides which server block should 
       # handle the request by matching the incoming Host header
       #  to the server_name directives defined in its configuration.
        # server_name sanjeev.com;
        #curl -H "Host: sanjeev.com" http://127.0.0.1

        location / {
               # allow 192.168.43.60; # this ip of the network can access
              #  deny all;
                proxy_pass http://localhost:8000;
                proxy_http_version 1.1;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection 'upgrade';
                proxy_set_header Host $http_host;
                proxy_set_header X-NginX-Proxy true;
                proxy_redirect off;
        }

}

# All ips are available in the network 
# will be proxyed to this http://localhost:8000


```








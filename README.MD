## Local To Docker Container Code Syncronization

The following code is used to synchronize the local code with the Docker container code. This is done by
1. Creating a new Docker container from the Docker image.
2. Copying the local code into the Docker container.
3. Changing any code in local computer and then copying it into the Docker container.
4. The Docker container will be synced with the local code.

### If we run our Docker Images with compose setup.We do not need to use any .env file.
### And composed container can not be ran using docker-desktop app.



## Docker Image Development Mode

### docker-compose.dev.yml


```python


services:

  bidyut:
      build: .
      ports:
        - "8000:8000"

      volumes:   # bind mount the current directory to container /app
       - ./:/app:ro
     
      command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
       # overriding the default starter command
            
      environment:
        - database_username=postgres
        - database_password=bidyut
        - database_host=postgres
        - database_port=5434
        - database_name=pybackend
        - SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        - ALGORITHM=HS256
        - ACCESS_TOKEN_EXPIRE_MINUTES=60

      depends_on:
      - postgres  # Ensures postgres is started before the bidyut service
     
 
  postgres:
    image: postgres:15
    environment:
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=bidyut
        - POSTGRES_DB=pybackend
    ports:
    - "5434:5434"
    volumes:
    - postgres-db:/var/lib/postgresql/data # Where we keep our  data  


volumes:
     postgres-db:  # multiple services can use the same volume



# docker compose -f  docker-compose-dev.yml up -d # To run the services in development and detached mode
```
```
#Commands:
docker compose -f  docker-compose-dev.yml up -d # to build and start the container in a detached mode
docker compose -f  docker-compose-dev.yml up -d --build #If we made changes to the image then it forces to build the image and starts the container.
docker compose -f  docker-compose-dev.yml down # stops the container



```


## Docker Image Production Mode

 - To use this image we need to have Environments varalbles set to the values we want to use in production.



### docker-compose.prod.yml


```python


services:

  bidyut:
      # build: .
      image: bidyutsikder/pybackend # use an image from Docker Hub (optional)
      ports:
        - "800:8000"  #production port out : docker expose port in 

      # volumes:   # We stoped bind mount the current directory to container /app
      #  - ./:/app:ro
     
      # command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
       # We stoped overriding the default starter command
            
      environment:
      # We can hard code the values here
        - database_username=postgres
        - database_password=bidyut
        - database_host=postgres
        - database_port=5434
        - database_name=pybackend
        - SECRET_KEY='09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
        - ALGORITHM=HS256
        - ACCESS_TOKEN_EXPIRE_MINUTES=60

        # Or We can use ubuntu system local environment variables here

        # Before useing this make sure you have all the environment variables set in your ubuntu system.
        # On your local computer using command ( printenv ) you can see all the variables you need. or use hard code values here

        # - database_username=${database_username}
        # - database_password=${database_password}
        # - database_host=${database_host}
        # - database_port=${database_port}
        # - database_name=${database_name}
        # - SECRET_KEY=${SECRET_KEY}
        # - ALGORITHM=${ALGORITHM}
        # - ACCESS_TOKEN_EXPIRE_MINUTES=${ACCESS_TOKEN_EXPIRE_MINUTES}


      depends_on:
      - postgres  # Ensures postgres is started before the bidyut service
     
 
  postgres:
    image: postgres:15
    environment:
         # - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=bidyut
        - POSTGRES_DB=pybackend

        # Or We can use ubuntu system local environment variables here
        # - POSTGRES_USER=postgres
        # - POSTGRES_PASSWORD=${database_password}
        # - POSTGRES_DB=${database_name}


    ports:
    - "5434:5434"
    volumes:
    - postgres-db:/var/lib/postgresql/data # Where we keep our  data  


volumes:
     postgres-db:  # multiple services can use the same volume





# docker compose -f  docker-compose-prod.yml up -d # To run the services in production and detached mode
```
***Here is the explanation of the code:***
- We are using the `docker-compose` tool to define and run multiple Docker containers.
- We have two services defined: `bidyut` and `postgres`.
- The `bidyut` service is a Python application that uses the `uvicorn` web server to
run the FastAPI application. It uses the `gunicorn` WSGI server to run
the application in production mode.


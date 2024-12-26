## Local To Docker Container Code Syncronization

The following code is used to synchronize the local code with the Docker container code. This is done by
1. Creating a new Docker container from the Docker image.
2. Copying the local code into the Docker container.
3. Changing any code in local computer and then copying it into the Docker container.
4. The Docker container will be synced with the local code.



### docker-compose.yml


```python

services:

  bidyut:
      build: .
      ports:
        - "8000:8000"

      volumes:
       - ./:/app:ro
     
      command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
       #overriding the default starter command
            
      environment:
        - database_username=postgres
        - database_password=bidyut
        - database_host=postgres
        - database_port=5434
        - database_name=pybackend
        - SECRET_KEY='09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
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


```

## Testing APIs with Pytest on Github Actions And Deploy

***conftest.py*** 
- This is a spicific file in the root of your project where you can put fixtures and other setup/teardown code that should be run for all tests in the project.
- If we have a folder within tests folder inside that folder we can have another conftest.py file.This is very usefull for scoping fixtures to specific test modules.

### Run the commands to run tests...
```python
pytest filePath --disable-warnings -v # To run specific file based test
pytest --disable-warnings -v # Gives Test results without warnings
pytest --disable-warnings -v -x # Stops Testing when faces an error.



```

## Github Actions

 - Create a new file in the root of your project called `.github/workflows/anyname.yml`
 - This file is used to define the workflow to Test,Deploy (CI/CD) for your project.
 - You can define multiple workflows in this file for different branchs.

```

# This workflow will install Python dependencies, run tests  with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python application

on:
  push:
    branches: [ "testing" ]
  pull_request:
    branches: [ "testing" ]

permissions:
  contents: read

jobs:
  build: # Job name
    environment:
      name: testing #This is the name of the environment list set for testing on github environment
    env: # These are from github secret.
      database_username : ${{secrets.DATABASE_USERNAME}} 
      database_password : ${{secrets.DATABASE_PASSWORD}}
      database_host : ${{secrets.DATABASE_HOST}}
      database_port : ${{secrets.DATABASE_PORT}}
      database_name : ${{secrets.DATABASE_NAME}}
      SECRET_KEY : ${{secrets.SECRET_KEY}}
      ALGORITHM : ${{secrets.ALGORITHM}}
      ACCESS_TOKEN_EXPIRE_MINUTES : ${{secrets.ACCESS_TOKEN_EXPIRE_MINUTES}}

    services: # This service will create a postgresql database server on github actions just like other docker container.(https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/creating-postgresql-service-containers)
      postgres: # This is the name of the service
        image: postgres # This is the image to use
        env:
          POSTGRES_PASSWORD: ${{secrets.DATABASE_PASSWORD}}
          POSTGRES_DB: ${{secrets.DATABASE_NAME}}_test
        ports:
          - 5432:5432 # This is the port to use
        
        options: >-
          --health-cmd="pg_isready" 
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5



    runs-on: ubuntu-latest
    steps:
    - name: pulling git repo
      uses: actions/checkout@v4
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install  pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Test with pytest
      run: |
        pytest 

## This part is for pushing the image to docker hub (https://docs.docker.com/build/ci/github-actions/)

    - name: Login to Docker Hub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKER_HUB_USERNAME }}
        password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3


    - name: Build and push
      uses: docker/build-push-action@v6
      with:
        context: ./
        file: ./Dockerfile
        tags: ${{ secrets.DOCKER_HUB_USERNAME }}/pybackend:latest
        push: true

  deploy: # Job name
    environment:
      name: production #This is the name of the environment list for production set on github environment
    runs-on: ubuntu-latest
    needs: [build] # This Deploy job will start when the build job is completed.
    steps:
      - name: Deploy to Render # github-marketplace (Render.com Deploy)
        uses: ttskch/render-deploy@v1.0.0
        with:
          api-key: ${{ secrets.RENDER_API_KEY }}
          service-id: ${{ secrets.RENDER_SERVICE_ID }}

      # - name: Deploy to Ubuntu Server # github-marketplace (appleboy SSH Remote Commands)
      #   uses: appleboy/ssh-action@v1.2.0
      #   with:
      #     host: ${{ secrets.PROD_HOST }} #your server ip
      #     username: linuxserver.io
      #     password: ${{ secrets.PROD_PASSWORD }} #your server password
      #     port: ${{ secrets.PROD_PORT }} #your server port
      #     script: |
      #       cd app/yourproject_path_on_remote_ubuntu_server
      #       git pull origin branchName
      #       echo ${{secrets.PROD_PASSWORD}} | sudo -S systemctl restart serviceName # Ubuntu server takes a prompt for password


```
## Testing APIs with Pytest on Github Actions

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
 - This file is used to define the workflow for your project.
 - You can define multiple workflows in this file for different branchs.

```



# This workflow will install Python dependencies, run tests and lint with a single version of Python
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
  build:
    environment:
      name: testing
    env: # These are from github secret.
      database_username : ${{secrets.DATABASE_USERNAME}} 
      database_password : ${{secrets.DATABASE_PASSWORD}}
      database_host : ${{secrets.DATABASE_HOST}}
      database_port : ${{secrets.DATABASE_PORT}}
      database_name : ${{secrets.DATABASE_NAME}}
      SECRET_KEY : ${{secrets.SECRET_KEY}}
      ALGORITHM : ${{secrets.ALGORITHM}}
      ACCESS_TOKEN_EXPIRE_MINUTES : ${{secrets.ACCESS_TOKEN_EXPIRE_MINUTES}}

    services: # This service will create a postgresql database server on github actions just like other docker container.
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
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Test with pytest
      run: |
        pytest 


```
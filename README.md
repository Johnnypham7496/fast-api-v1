# Fast-api-v1
rewriting enterprise level fast-api

## commands used for setup 
- Setup 

    - py -3 -m venv venv 

    - . venv/Scripts/activate 

    - pip install fastapi 

    - pip install uvicorn 

    - pip freeze > requirements.txt

- Pytest

    - pip install pytest

    - pip install httpx

- Sqlalchemy

    pip install sqlalchemy

## Initial commit 
is to have the venv installed and updated readme
<hr>

## Added requirements.txt
adding a file called requirements.txt for dependency management
<hr>

## Created main.py file
created main.py file to run endpoint and test to make sure our code runs

<img src="images/hello_world.png" alt="hello world" width="400" height="250">
<hr>

## Swagger spec documentation
swagger ui is included in FastAPI meaning we don't have to write it out from scratch like Flask

<img src="images/fastapi_swagger.png" alt="FastAPI swagger title" height="200" width="600">
<hr>

## Created app_test.py in tests folder 
testing welcome path op

<img src="images/test_tc0001_welcome.png" alt="test_tc0001_welcome" height="200" width="">

## Created health enpoint and created a test for this endpoint

<img src="images/health.png" alt="health" height="200" width="900">

<img src="images/health_test.png" alt="health_test" height="200" width="">
<hr>

## Installed sqlalchemy dependency and created a db_config file for database connection
<hr>


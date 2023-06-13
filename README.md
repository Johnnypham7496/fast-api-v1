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

## Creating users data table 
id column is generated after the other 2 fields are entered
primary key makes it easier for us to find the user
string(#) will alow how many characters are entered
unique ensuring there is one 1 particular value in the database
nullable meaning this field is required 

<img src="images/users_table.png" alt="health_test" height="200" width="">
<hr>

## Created schema.py
this is for when someone is entering data, the data will be bumped against the schema to make sure all fields are present before interacting with the database

orm stands for object realational mapping

<img src="images/user_model.png" alt="user_model" height="250" width="">
<hr>

## Created user_repository.py file
this file will have the functions we need to interact with the database
this will also have a test data function for testing

<img src="images/user_repository.png" alt="user_repository" height="300" width="">
<hr>

## Created a create_db function
this function is for creating our db file in db/local_sqlite

this will drop_all data at first then create the data and add the test data

<img src="images/create_db.png" alt="create_db" height="200" width="700">
<hr>

## Moved welcome and health endpoint to app_router.py located in the router folder
<hr>

## Created get_all_users function in user_repository.py
this code allows us to retrieve all the users in the database
also added a function in the users_router.py for users to access

<img src="images/get_all_users.png" alt="get_all_users" height="150" width="400">
<hr>

# Created get_all_users test in users_test.py
this test is will be testing the first data in our test.db making sure all the values are present

<img src="images/test_get_all_users.png" alt="test_get_all_users" height="350" width="500">
<hr>


## Created get_by_username function in user_repository.py and get_by_username path operation in users_router
these codes will allow us to get information from a single user by their username 

<img src="images/get_by_username.png" alt="test_get_all_users" height="250" width="1000">
<img src="images/get_by_username_repository.png" alt="test_get_all_users" height="200" width="500">
<hr>

## Created get_by_username test in users_test.py file testing the 200 and 404 response codes and return messages
<hr>
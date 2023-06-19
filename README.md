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

## 01. Initial commit 
is to have the venv installed and updated readme
<hr>

## 02. Added requirements.txt
adding a file called requirements.txt for dependency management
<hr>

## 03. Created main.py file
created main.py file to run endpoint and test to make sure our code runs

<img src="images/hello_world.png" alt="hello world" width="400" height="250">
<hr>

## 04. Swagger spec documentation
swagger ui is included in FastAPI meaning we don't have to write it out from scratch like Flask

<img src="images/fastapi_swagger.png" alt="FastAPI swagger title" height="200" width="600">
<hr>

## 05. Created app_test.py in tests folder 
testing welcome path op

<img src="images/test_tc0001_welcome.png" alt="test_tc0001_welcome" height="200" width="">

## 06. Created health enpoint and created a test for this endpoint

<img src="images/health.png" alt="health" height="200" width="900">

<img src="images/health_test.png" alt="health_test" height="200" width="">
<hr>

## 07. Installed sqlalchemy dependency and created a db_config file for database connection
<hr>

## 08. Creating users data table 
id column is generated after the other 2 fields are entered
primary key makes it easier for us to find the user
string(#) will alow how many characters are entered
unique ensuring there is one 1 particular value in the database
nullable meaning this field is required 

<img src="images/users_table.png" alt="health_test" height="200" width="">
<hr>

## 09. Created schema.py
this is for when someone is entering data, the data will be bumped against the schema to make sure all fields are present before interacting with the database

orm stands for object realational mapping

<img src="images/user_model.png" alt="user_model" height="250" width="">
<hr>

## 10. Created user_repository.py file
this file will have the functions we need to interact with the database
this will also have a test data function for testing

<img src="images/user_repository.png" alt="user_repository" height="300" width="">
<hr>

## 11. Created a create_db function
this function is for creating our db file in db/local_sqlite

this will drop_all data at first then create the data and add the test data

<img src="images/create_db.png" alt="create_db" height="200" width="700">
<hr>

## 12. Moved welcome and health endpoint to app_router.py located in the router folder
<hr>

## 13. Created get_all_users function in user_repository.py
this code allows us to retrieve all the users in the database
also added a function in the users_router.py for users to access

<img src="images/get_all_users.png" alt="get_all_users" height="150" width="400">
<hr>

## 14. Created get_all_users test in users_test.py
this test is will be testing the first data in our test.db making sure all the values are present

<img src="images/test_get_all_users.png" alt="test_get_all_users" height="350" width="500">
<hr>


## 15. Created get_by_username function in user_repository.py and get_by_username path operation in users_router
these codes will allow us to get information from a single user by their username 

<img src="images/get_by_username.png" alt="test_get_all_users" height="250" width="1000">
<img src="images/get_by_username_repository.png" alt="test_get_all_users" height="200" width="500">
<hr>

## 16. Created get_by_username test in users_test.py file testing the 200 and 404 response codes and return messages
<hr>

## 17. Created add_user function in users_router.py file and created a CreateUserModel in schemas.py prompting the user to enter in the required fields before creating user to the database
<hr>

## 18. Created add_user function to users_test.py file
this test will test our post operation in users_router.py and will also preform a get call to check the user information that is created in test.db file
<hr>

## 19. Created different scenario tests for add_user function in users_router.py
testing different fields to make sure a status_code of 400 is responded to user when not entering all fields for post request
<hr>

## 20. Added update_user function to users_repository.py
this code will udpate the fields if values are given by the user. We do not want the user to be able to update the username but email and role fields can be updated 

<img src= "images/update_user.png" alt="update_user" height="250" width="600">
<hr>


## Created update_user function in users_router.py file
this function check if there is a value in the email and role fields, then check to for the username within our database, will check there are values entered by the user in both email and role otherwise the fields will not be updated, also checks if both fields are empty

If email or role values are added or both, this will give a 204 status_code and will commit these changes in our database
<hr>

## Added put user test in users_test.py
testing different areas for put request such as updating both fields or email and role and testing if put request works if we only have 1 field being changed

added more put test by testing the bad scenarios if they body is empty, username not found, and if there is no body in the request
<hr>
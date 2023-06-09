from fastapi import FastAPI, Response, status

# creating app variable for path operations
app = FastAPI(
    title="Johnny's-FastAPI",
    description="This is the swagger spec for the FastApi workshop",
    version='1.0.0'
)


# get path operation for welcome message. Tags and response_description are for swagger ui documentation
@app.get("/", tags=["Welcome"], response_description="Displays Welcome message")  
async def welcome(response: Response):
    response.status_code = status.HTTP_200_OK
#   when a user hits this endpoint, the status_response should be a 200 and will return a message for the user
#   response parameter inside the function is for HTTP status codes
    return {"message": "Hello, welcome to Autobots FastAPI bootcamp"}


@app.get("/health", tags=['health'], response_description='Retrieves health status of this application')
async def health(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": "OK"}
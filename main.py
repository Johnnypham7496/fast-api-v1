import uvicorn 
from fastapi import FastAPI, Response, Depends
from router import app_router, users_router
from db import user_db
from db_config import engine, get_db
from repository import users_repository
from sqlalchemy.orm import Session


# creating app variable for path operations
app = FastAPI(
    title="Johnny's-FastAPI",
    description="This is the swagger spec for the FastApi workshop",
    version='1.0.0'
)


app.include_router(app_router.router)
app.include_router(users_router.router)


# @app.get("/dbsetup")
# def create_db(db: Session = Depends(get_db)):
#     user_db.Base.metadata.drop_all(engine)
#     user_db.Base.metadata.create_all(engine)
#     users_repository.add_user_td(db)
#     response_text = '{"message": "Database created."}'
#     response = Response(content=response_text, status_code=200, media_type='application/json')
#     return response


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
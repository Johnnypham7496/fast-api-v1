from sqlalchemy import String, Integer, Column
from db_config import Base 

# creating a users table with 4 columns
class Userdb(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index= True)
    username = Column(String(120), unique=True, nullable= False)
    email = Column(String(120), unique=True, nullable= False)
    role = Column(String(120), unique=False, nullable= False)
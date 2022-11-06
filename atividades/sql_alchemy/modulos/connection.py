import sqlalchemy as sa
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv
import os

load_dotenv('/.env')

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)
from datetime import datetime as dt

host=os.getenv('host')
port=os.getenv('port')
user=os.getenv('user')
passwd=os.getenv('Passwd')
db=os.getenv('db')

engine = create_engine(
    url=f'mysql+mysqlconnector://{user}{host}:{port}/{db}',
)


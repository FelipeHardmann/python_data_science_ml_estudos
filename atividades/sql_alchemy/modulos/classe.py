import connection
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)
import sqlalchemy as sa

Base = declarative_base()

class Product(Base):
    __tablename__: str = 'products'

    
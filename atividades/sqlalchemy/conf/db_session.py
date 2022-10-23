# Importando libs
from re import S
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
from models.model_base import ModelBase

__engine: Optional[Engine] = None

def create_engine() -> Engine:
    '''Função para configurar a conexão com o Banco de dados'''
    global __engine 
    if __engine:
        return

    conn_str = 'mysql+mysqlconnector://root:@localhost:3306/PICOLES'
    __engine = sa.create_engine(url=conn_str, echo=False)

def create_session() -> Session:
    '''Função para criar a sessão de conexão ao banco de dados'''
    global __engine
    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()
    return session

def create_tables() -> None:
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models

    ModelBase.metadata.drop_all()
    ModelBase.metadata.create_all()

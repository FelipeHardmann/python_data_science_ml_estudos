from enum import unique
import sqlalchemy as sa
from datetime import datetime
from model_base import ModelBase

class AditivoNutritivo(ModelBase):
    __tablename__: str = 'aditivos_nutritivos'

    id: int = sa.Column(sa.BigInteger(), primary_key=True, autoincremente=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now)
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    gormula_quimica: str = sa.Column(sa.String(45), unique=True, nullable=False)
    alergenicos: str = sa.Column(sa.String(45), nullable=True)

    def ___repr__(self):
        return f'<Aditivo Nutritivo: {self.nome}>'

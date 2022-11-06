import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

from datetime import datetime as dt

# Conectando ao banco de dados
# echo=True mostra no terminal os comandos SQL
engine = create_engine(
    url = 'mysql+mysqlconnector://root@localhost:3306/INFINITY',
    echo = True
)

# Declarando o mapeamento
Base = declarative_base()

class Product(Base):
    # Nome da tabela(Create table)
    __tablename__: str = 'products'
    # Criando as colunas
    id: int = sa.Column(sa.Integer, primary_key=True)
    creation_date: dt = sa.Column(sa.DateTime, default=dt.now)
    name: str = sa.Column(sa.String(30), nullable=False)
    color: str = sa.Column(sa.String(20), nullable=False)
    price: float = sa.Column(sa.DECIMAL(6, 2), nullable=False)
    quantity: int = sa.Column(sa.Integer, nullable=False)
    description: str = sa.Column(sa.String(50))

    def __repr__(self) -> str:
        '''Retorna a representação do objeto'''
        return f'<{self.name} {self.color}>'

# Criar tabela no BD
Base.metadata.create_all(engine)

# Criando a Sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criando um objeto e adicionando argumentos nomeados  
# prd = Product(
#     name = 'Camiseta',
#     color = 'Azul',
#     price = 98.30,
#     quantity = 10,
#     description = 'Camiseta de algodão de meia manga'
# )

# session.add(prd)
# session.commit()

# Inserindo vários
# session.add_all([
#     Product(
#         name='Short',
#         color = 'Jeans',
#         price = 58,
#         quantity = 15,
#         description = 'Short jeans feminino'
#         ),
#     Product(
#         name = 'Calça',
#         color = 'Preta',
#         price = 120.02,
#         quantity = 20,
#         description = 'Calça moletom'
#     )
# ])
# session.commit()

# Recuperando dados
# query = session.query(Product).all()
# print(f'Produtos: ')
# for dados in query:
#     print(f'Name: {dados.name} {dados.color}')
#     print(f'Price: R${dados.price}')
#     print(f'Quantity: {dados.quantity}')
#     print(f'Description: {dados.description}')


# Filtrando produtos(Where em SQL)
# query = session.query(Product).filter_by(name = 'Camiseta').first()
# print(query.name, query.price, sep='-----')

# Update de dados 
# query = session.query(Product).filter_by(name='Short').first()
# query.description = 'Short jeans'
# session.commit()

# Removendo dados
# produto = session.query(Product).filter_by(name = 'Calça').first()
# session.delete(produto)
# session.commit()

total = session.query(Product).count()
print(f'A quantidade de produtos: {total}')
from sqlalchemy import Column, Integer, String, Date
from .database import Base

class PessoaDB(Base):
    __tablename__ = "pessoas"
    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String)
    data_nascimento = Column(Date)
    sexo = Column(String)
    email = Column(String, unique=True, index=True)
    celular = Column(String)

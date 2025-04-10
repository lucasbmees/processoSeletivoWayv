from sqlalchemy import Column, Integer, String, Date
from .database import Base

class PessoaDB(Base):
    """
    Modelo de banco de dados para representar uma Pessoa na tabela 'pessoas'.

    Este modelo é utilizado para armazenar as informações dos participantes
    importados via Excel ou recebidos por Webhook.

    Campos:
    - id: Identificador único (chave primária).
    - nome_completo: Nome completo do participante.
    - data_nascimento: Data de nascimento no formato YYYY-MM-DD.
    - sexo: Gênero (ex: Masculino, Feminino, Outros).
    - email: Endereço de e-mail (único e indexado).
    - celular: Número de celular com DDD.
    """
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String)
    data_nascimento = Column(Date)
    sexo = Column(String)
    email = Column(String, unique=True, index=True)
    celular = Column(String)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados SQLite.
# O banco será armazenado no arquivo local "banco.db".
DATABASE_URL = "sqlite:///./banco.db"

# Cria o engine do SQLAlchemy, responsável por conectar ao banco de dados.
# O parâmetro "check_same_thread=False" é necessário para permitir múltiplas threads acessando o SQLite (como o FastAPI faz).
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma fábrica de sessões (SessionLocal) para interagir com o banco de dados.
# Cada instância de sessão será usada nas rotas para inserir, consultar, atualizar ou excluir dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa usada para definir os modelos das tabelas do banco.
# Todas as classes de modelo (como PessoaDB) devem herdar desta classe Base.
Base = declarative_base()

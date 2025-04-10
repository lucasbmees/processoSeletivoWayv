from fastapi import FastAPI
from .database import Base, engine
from .models import PessoaDB
from .routes import excel, listar, atualizar, webhook, limpar

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

# Instância principal da API com documentação aprimorada
app = FastAPI(
    title="API de Participantes - Processo Seletivo",
    description="""
Esta API permite o gerenciamento de uma base de participantes. Com ela, é possível:

- Inserir dados via planilha Excel
- Listar participantes com filtros
- Atualizar dados de nascimento
- Receber informações via Webhook
- Limpar toda a base

Desenvolvida em FastAPI + SQLite como parte de um teste técnico.
""",
    version="1.0.0",
    contact={
        "name": "Lucas Borinelli Mees",
        "email": "lucasbmees8@gmail.com"
    },
    docs_url="/docs",       # Rota Swagger UI
    redoc_url="/redoc"      # Rota Redoc
)

@app.get("/", summary="Status da API", tags=["Root"])
def read_root():
    """
    Retorna uma mensagem de status para confirmar que a API está no ar.
    """
    return {"mensagem": "API com SQLite está no ar!"}

# Registro de rotas organizadas por funcionalidade
app.include_router(excel.router, tags=["Upload Excel"])
app.include_router(listar.router, tags=["Listagem"])
app.include_router(atualizar.router, tags=["Atualização"])
app.include_router(webhook.router, tags=["Webhook"])
app.include_router(limpar.router, tags=["Limpeza"])

from fastapi import FastAPI
from .database import Base, engine
from .models import PessoaDB
from .routes import excel, listar, atualizar, webhook, limpar

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API com SQLite")

@app.get("/")
def read_root():
    return {"mensagem": "API com SQLite está no ar!"}

# Registro de rotas
app.include_router(excel.router)
app.include_router(listar.router)
app.include_router(atualizar.router)
app.include_router(webhook.router)
app.include_router(limpar.router)

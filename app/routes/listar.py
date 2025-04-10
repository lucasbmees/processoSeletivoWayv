from fastapi import APIRouter, Query
from typing import Literal
from ..models import PessoaDB
from ..database import SessionLocal

router = APIRouter()

@router.get("/listar")
def listar_pessoas(sexo: Literal["Masculino", "Feminino", "Outros"] = None):
    session = SessionLocal()
    if sexo:
        pessoas = session.query(PessoaDB).filter(PessoaDB.sexo == sexo).all()
    else:
        pessoas = session.query(PessoaDB).all()
    session.close()
    return pessoas

from fastapi import APIRouter, Query
from typing import Literal
from ..models import PessoaDB
from ..database import SessionLocal

router = APIRouter()

@router.get(
    "/listar",
    summary="Listar pessoas cadastradas",
    response_description="Lista de pessoas cadastradas no banco de dados"
)
def listar_pessoas(sexo: Literal["Masculino", "Feminino", "Outros"] = None):
    """
    Retorna uma lista de pessoas cadastradas.

    - Pode ser filtrado pelo campo **sexo** (Masculino, Feminino ou Outros).
    - Se nenhum filtro for passado, todas as pessoas são listadas.

    **Parâmetros:**
    - **sexo** (opcional): Filtro pelo sexo da pessoa.

    **Retorna:** Lista de registros com nome, data de nascimento, sexo, e-mail e celular.
    """
    session = SessionLocal()
    if sexo:
        pessoas = session.query(PessoaDB).filter(PessoaDB.sexo == sexo).all()
    else:
        pessoas = session.query(PessoaDB).all()
    session.close()
    return pessoas

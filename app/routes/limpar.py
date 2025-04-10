from fastapi import APIRouter
from ..models import PessoaDB
from ..database import SessionLocal

router = APIRouter()

@router.delete("/limpar")
def limpar_base():
    session = SessionLocal()
    session.query(PessoaDB).delete()
    session.commit()
    session.close()
    return {"mensagem": "Todos os registros foram removidos com sucesso."}

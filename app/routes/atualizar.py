from fastapi import APIRouter, HTTPException
from datetime import date
from ..models import PessoaDB
from ..database import SessionLocal

router = APIRouter()

@router.put("/atualizar_data/{email}")
def atualizar_data_nascimento(email: str, nova_data: date):
    session = SessionLocal()
    pessoa = session.query(PessoaDB).filter(PessoaDB.email == email).first()
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    pessoa.data_nascimento = nova_data
    session.commit()
    session.close()
    return {"mensagem": "Data de nascimento atualizada com sucesso."}

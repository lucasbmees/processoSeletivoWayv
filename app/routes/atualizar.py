from fastapi import APIRouter, HTTPException
from datetime import date
from ..models import PessoaDB
from ..database import SessionLocal

router = APIRouter()

@router.put(
    "/atualizar_data/{email}",
    summary="Atualizar data de nascimento",
    response_description="Mensagem de sucesso ao atualizar a data"
)
def atualizar_data_nascimento(email: str, nova_data: date):
    """
    Atualiza a data de nascimento de uma pessoa a partir do e-mail informado.

    **Parâmetros:**
    - **email**: E-mail da pessoa que será atualizada (passado na URL)
    - **nova_data**: Nova data de nascimento no formato `YYYY-MM-DD` (passado como parâmetro query)

    **Retorna:** mensagem de sucesso se o e-mail for encontrado e atualizado.

    **Erros possíveis:**
    - `404`: Pessoa não encontrada com o e-mail informado
    """
    session = SessionLocal()
    pessoa = session.query(PessoaDB).filter(PessoaDB.email == email).first()
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")
    pessoa.data_nascimento = nova_data
    session.commit()
    session.close()
    return {"mensagem": "Data de nascimento atualizada com sucesso."}

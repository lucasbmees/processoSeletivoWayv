from fastapi import APIRouter
from ..models import PessoaDB
from ..database import SessionLocal

router = APIRouter()

@router.delete(
    "/limpar",
    summary="Remover todos os registros",
    response_description="Mensagem de sucesso após limpar a base de dados"
)
def limpar_base():
    """
    Remove todos os registros da base de dados.

    Esta operação deleta permanentemente todos os dados da tabela `pessoas`.

    **Atenção:** essa ação é irreversível.

    **Retorna:** mensagem de confirmação.
    """
    session = SessionLocal()
    session.query(PessoaDB).delete()
    session.commit()
    session.close()
    return {"mensagem": "Todos os registros foram removidos com sucesso."}

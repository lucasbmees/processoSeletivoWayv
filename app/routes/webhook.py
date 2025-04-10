from fastapi import APIRouter
from datetime import date
from ..schemas import Pessoa

router = APIRouter()

@router.post("/webhook", summary="Receber dados via Webhook", response_description="Idade calculada a partir da data de nascimento")
def receber_webhook(dados: Pessoa):
    """
    Recebe os dados de uma pessoa via requisição POST e calcula a idade com base na data de nascimento.

    - **nome_completo**: Nome completo da pessoa
    - **data_nascimento**: Data de nascimento (formato ISO: YYYY-MM-DD)
    - **sexo**: Masculino, Feminino ou Outros
    - **email**: E-mail válido
    - **celular**: Número de celular

    Retorna a idade calculada com base na data atual.
    """
    hoje = date.today()
    idade = hoje.year - dados.data_nascimento.year - (
        (hoje.month, hoje.day) < (dados.data_nascimento.month, dados.data_nascimento.day)
    )
    return {
        "mensagem": "Dados recebidos via webhook",
        "idade_calculada": idade
    }

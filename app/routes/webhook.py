from fastapi import APIRouter
from datetime import date
from ..schemas import Pessoa

router = APIRouter()

@router.post("/webhook")
def receber_webhook(dados: Pessoa):
    hoje = date.today()
    idade = hoje.year - dados.data_nascimento.year - ((hoje.month, hoje.day) < (dados.data_nascimento.month, dados.data_nascimento.day))
    return {"mensagem": "Dados recebidos via webhook", "idade_calculada": idade}

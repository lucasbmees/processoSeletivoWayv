from pydantic import BaseModel, EmailStr
from typing import Literal
from datetime import date

class Pessoa(BaseModel):
    """
    Modelo de validação de dados para criação e recebimento de informações de uma pessoa.

    Este modelo é utilizado para validar os dados recebidos via API (por exemplo, nos endpoints
    de inserção, webhook ou atualização).

    Campos:
    - nome_completo: Nome completo da pessoa.
    - data_nascimento: Data de nascimento no formato YYYY-MM-DD.
    - sexo: Sexo da pessoa. Deve ser um dos seguintes valores: "Masculino", "Feminino", "Outros".
    - email: Endereço de e-mail válido (validação automática do formato).
    - celular: Número de celular com DDD (formato livre, mas obrigatório).
    """

    nome_completo: str
    data_nascimento: date
    sexo: Literal["Masculino", "Feminino", "Outros"]
    email: EmailStr
    celular: str

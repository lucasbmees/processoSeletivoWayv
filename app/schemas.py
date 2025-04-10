from pydantic import BaseModel, EmailStr
from typing import Literal
from datetime import date

class Pessoa(BaseModel):
    nome_completo: str
    data_nascimento: date
    sexo: Literal["Masculino", "Feminino", "Outros"]
    email: EmailStr
    celular: str

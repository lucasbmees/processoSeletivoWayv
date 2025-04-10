# 🧪 API de Gerenciamento de Participantes

Esta API foi desenvolvida como parte de um teste técnico para avaliação de habilidades em FastAPI, SQLite, organização de código, ingestão de dados via Excel, filtros, atualização, recebimento via webhook e limpeza de base.

---

## Funcionalidades

-  Inserção de dados via upload de planilha Excel
-  Listagem de participantes com filtro por sexo
-  Atualização da data de nascimento por e-mail
-  Webhook para recebimento de dados e cálculo de idade
-  Limpeza completa da base de dados
-  Banco de dados em SQLite

---

##  Como rodar o projeto

### 1. Clone o repositório
git clone https://github.com/lucasbmees/processoSeletivoWayv
cd processoSeletivoWayv/app

### 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

### 3. Instale as dependências
pip install fastapi uvicorn pandas openpyxl sqlalchemy pydantic

### 4. Rode a aplicação
uvicorn main:app --reload

---

## Estrutura do Projeto

app/
│
├── main.py               # Ponto de entrada da aplicação
├── database.py           # Configuração do SQLite e session
├── models.py             # Modelos SQLAlchemy e Pydantic
├── routes/
│   ├── excel.py          # Upload e inserção via Excel
│   ├── listar.py         # Listagem com filtro por sexo
│   ├── atualizar.py      # Atualização da data de nascimento
│   ├── webhook.py        # Webhook para receber dados
│   └── limpar.py         # Limpeza da base de dados


from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from ..schemas import Pessoa
from ..models import PessoaDB
from ..database import SessionLocal
import pandas as pd

router = APIRouter()

@router.post("/inserir_excel")
async def inserir_excel(arquivo: UploadFile = File(...)):
    if not arquivo.filename.endswith((".xls", ".xlsx")):
        raise HTTPException(status_code=400, detail="O arquivo deve ser .xls ou .xlsx")

    try:
        df = pd.read_excel(arquivo.file)
        df.columns = [col.strip().lower() for col in df.columns]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao ler o Excel: {str(e)}")

    session = SessionLocal()
    inseridos = 0
    for _, linha in df.iterrows():
        try:
            pessoa = Pessoa(
                nome_completo=linha["nome completo"].strip(),
                data_nascimento=pd.to_datetime(str(linha["data de nascimento"]).strip()).date(),
                sexo=linha["sexo"].strip(),
                email=linha["e-mail"].strip(),
                celular=linha["celular"].strip()
            )
            pessoa_db = PessoaDB(**pessoa.dict())
            session.add(pessoa_db)
            inseridos += 1
        except Exception as e:
            session.rollback()
            return JSONResponse(
                status_code=400,
                content={"erro": f"Erro ao processar linha: {linha.to_dict()}", "detalhes": str(e)}
            )
    session.commit()
    session.close()
    return {"mensagem": "Dados inseridos com sucesso!", "total_inseridos": inseridos}

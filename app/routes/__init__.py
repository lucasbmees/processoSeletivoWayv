from fastapi import APIRouter
from app.routes import excel, listar, limpar, atualizar, webhook

router = APIRouter()

router.include_router(excel.router, tags=["Excel"])
router.include_router(listar.router, tags=["Listagem"])
router.include_router(limpar.router, tags=["Administração"])
router.include_router(atualizar.router, tags=["Atualização"])
router.include_router(webhook.router, tags=["Webhook"])

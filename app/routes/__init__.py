from fastapi import APIRouter
from app.routes import excel, listar, limpar, atualizar, webhook

router = APIRouter()
router.include_router(excel.router)
router.include_router(listar.router)
router.include_router(limpar.router)
router.include_router(atualizar.router)
router.include_router(webhook.router)

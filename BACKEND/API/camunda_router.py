import requests
from fastapi import APIRouter
from SERVICES.camunda_service import iniciar_proceso

router = APIRouter()

@router.post("/iniciar-proceso")
def iniciar(data: dict):
    return iniciar_proceso(data)
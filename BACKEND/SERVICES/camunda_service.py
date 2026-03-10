import requests
from fastapi import HTTPException
from CONFIGURACION.config import CAMUNDA_BASE_URL,CAMUNDA_LOGIN_URL,CAMUNDA_USER,CAMUNDA_PASSWORD
 


def iniciar_proceso(payload: dict):

     response = requests.post(
            f"{CAMUNDA_BASE_URL}/v2/process-instances",
            json=payload
        )


     return response.json()

#src\main\resources\com\prisma\scoring\rules

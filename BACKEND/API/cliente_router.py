from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from DATABASE.config import get_db
from SERVICES import cliente_service
from SCHEMAS.schema_cliente import ClienteOut

router = APIRouter()

@router.get("/listar-cliente", response_model=list[ClienteOut])
async def obtener_clientes(
    db: AsyncSession = Depends(get_db)
):
    return await cliente_service.listar_clientes(db)


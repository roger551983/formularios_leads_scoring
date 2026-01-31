from fastapi import  APIRouter, Depends, HTTPException
from DATABASE.config import get_db
from SERVICES import prueba_service
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/pruebaConexion")
async def health_db(db: AsyncSession = Depends(get_db)):
    ok = await prueba_service.prueba_conexion(db)
    if not ok:
        raise HTTPException(status_code=500, detail="No hay conexión con PostgreSQL")
    return {"status": "ok", "database": "connected"}
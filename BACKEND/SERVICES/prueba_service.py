from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def prueba_conexion(db: AsyncSession):

    try:
        result = await db.execute(text("SELECT 1"))
        return result.scalar() == 1
    except Exception as e:
        print("Error de conexión:", e)
        return False
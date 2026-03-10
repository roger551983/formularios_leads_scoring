
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from MODELS.cliente import Cliente


async def listar_clientes(db: AsyncSession):
        result = await db.execute(select(Cliente))
        return result.scalars().all()
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "CONFIGURACION" / "variables_entorno.env"

load_dotenv(ENV_PATH, override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine( 
    DATABASE_URL,
    echo=True,
    poolclass=NullPool,
)

AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)
class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "CONFIGURACION" / "variables_entorno.env"

load_dotenv(ENV_PATH, override=True)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print(DATABASE_URL)

#DATABASE_URL = os.getenv("DATABASE_URL")

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


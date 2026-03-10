from sqlalchemy import Column, Integer, String
from DATABASE.config import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True)
    nombre_cliente = Column(String)
    email=Column(String)
    ingresos = Column(Integer)
    ratioDeuda =Column(Integer)
    scoreBuro=Column(Integer)

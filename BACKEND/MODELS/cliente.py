from sqlalchemy import Column, Integer, String
from DATABASE.config import Base

class Cliente(Base):
    __tablename__ = "cliente"
    __table_args__ = {"schema": "cliente"}


    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    email=Column(String)
    ingresos = Column(Integer)
    ratio_deuda =Column(Integer)
    score_buro=Column(Integer)

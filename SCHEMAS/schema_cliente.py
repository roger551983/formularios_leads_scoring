from pydantic import BaseModel

class ClienteOut(BaseModel):

    id : int
    nombre_cliente :str
    email:str
    ingresos : int
    ratioDeuda :int
    scoreBuro:int 

    class Config:
        from_attributes = True
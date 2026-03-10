from pydantic import BaseModel

class ClienteOut(BaseModel):

    id : int
    nombre :str
    email:str
    ingresos : int
    ratio_deuda :int
    score_buro:int 

    class Config:
        from_attributes = True
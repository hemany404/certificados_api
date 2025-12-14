from pydantic import BaseModel
from typing import Optional
from datetime import date


class InstituicaoSchema(BaseModel):
    nome : str
    email : str
    senha : str
    logo_url : Optional[str] 


    class config:
        from_attributes = True

class CertificadoSchema(BaseModel):
    aluno: str
    curso:str
    carga_horaria:int
    data_emissao: date
    instituicao_id:int

    class config:
        from_attributes = True  
    

class LoginSchema(BaseModel):
    email: str
    senha: str

    class config:
        from_attributes = True    



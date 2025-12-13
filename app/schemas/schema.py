from pydantic import BaseModel
from typing import Optional


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
    nota_final:int
    instituicao_id:int

    class config:
        from_attributes = True  
    

class LoginSchema(BaseModel):
    email: str
    senha: str

    class config:
        from_attributes = True    



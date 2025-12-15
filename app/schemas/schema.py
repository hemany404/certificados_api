from pydantic import BaseModel
from typing import Optional
from datetime import date


class InstituicaoSchema(BaseModel):
    nome : str
    email : str
    senha : str
    logo_url : Optional[str] =None


    class config:
        from_attributes = True

class CertificadoSchema(BaseModel):
    nome_aluno: str
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

class InstituicaoSchemaS(BaseModel):
    nome : str
 

    class config:
        from_attributes = True

   
class CertificadoSaida(BaseModel):
    nome_aluno: str
    curso: str
    hash: str
    carga_horaria :str
    data_emissao :str
    instituicao: InstituicaoSchemaS

    observacoes: Optional[str]

    class Config:
        from_attributes = True


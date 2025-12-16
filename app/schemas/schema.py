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
    carga_horaria :int
    data_emissao :date
    instituicao: InstituicaoSchemaS
    observacao: str = "Certificado Válido ✅"

   

    class Config:
        from_attributes = True


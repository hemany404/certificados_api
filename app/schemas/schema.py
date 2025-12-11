from pydantic import BaseModel

class InstituicaoSchema(BaseModel):
    nome : str
    email = str
    senha = str


    class config:
        from_attributes = True

class CertificadoSchema(BaseModel):
    aluno: str
    curso:str
    nota_final:int
    instituicao_id:int



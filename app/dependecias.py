from fastapi import Depends,HTTPException
from sqlalchemy.orm import  session
from app.models.modelos import Instituicao
from main import ALGORITHM,SECRETY_KEY,oauth2_schema
from jose import jwt,JWTError
from app.core.database import pegar_db

def verificar_usuario(token: str = Depends(oauth2_schema), session: session = Depends(pegar_db)):
    try:
        dic_info = jwt.decode(token,SECRETY_KEY,ALGORITHM)
        id_instituicao = int(dic_info.get("sub"))
    except JWTError:    
        raise HTTPException(status_code=401, detail="acesso negado,verifica a data do token")
    instituicao = session.query(Instituicao).filter(Instituicao.id == id_instituicao).first()
    if not instituicao:
        raise  HTTPException(status_code=401,detail="usuario não encontrado")
    return instituicao
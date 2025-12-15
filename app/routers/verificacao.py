from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import pegar_db
from app.crud import obter_certificado_pelo_hash
from app.schemas.schema import CertificadoSaida

roteador_verificacao = APIRouter(tags=["verificacao"])

@roteador_verificacao.get("/verificar/{codigo_hash}", response_model=CertificadoSaida)
def verificar(codigo_hash: str, db: Session = Depends(pegar_db)):
    certificado = obter_certificado_pelo_hash(db, codigo_hash)
    if not certificado:
        raise HTTPException(status_code=404, detail="Certificado não encontrado")
    return certificado

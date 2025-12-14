from fastapi import APIRouter,Depends,HTTPException
from app.dependecias import verificar_usuario
from schemas.schema import CertificadoSchema
from models.modelos import Certificado,Instituicao
from sqlalchemy.orm import session
from app.core.database import pegar_db

certificado_roteador = APIRouter(prefix="certificados", tags=["certificado"])

@certificado_roteador.post("/certicado/emitir")
async def emitir_certicado(certificado_schema: CertificadoSchema,session:session=Depends(pegar_db),instituicao:Instituicao=Depends(verificar_usuario)):
    instituicao = session.query(Instituicao).filter(Instituicao.id == instituicao.id).first()

    if not instituicao:
        raise HTTPException(status_code=400,detail="está instituição não existe")
    
    novo_certificado = Certificado()
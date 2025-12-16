from fastapi import APIRouter,Depends,HTTPException
from app.dependecias import verificar_usuario
from app.schemas.schema import CertificadoSchema
from app.models.modelos import Certificado,Instituicao
from app.utils.gerar_hash import gerar_hash
from app.utils.gerar_qrcode import gerar_qr
from app.services.storage import local_path_url
from app.services.gerar_pdf import gerar_pdf_certificado
from sqlalchemy.orm import session
from app.utils.gerar_qrcode import gerar_qr
from app.crud import criar_certificado_na_bd,actualizar_caminho
from app.core.database import pegar_db

certificado_roteador = APIRouter(prefix="/certificados", tags=["certificado"])

@certificado_roteador.post("/certicado/emitir")
async def emitir_certicado(certificado_schema: CertificadoSchema,session:session=Depends(pegar_db),instituicao:Instituicao=Depends(verificar_usuario)):
    instituicao = session.query(Instituicao).filter(Instituicao.id == instituicao.id).first()

    if not instituicao:
        raise HTTPException(status_code=400,detail="está instituição não existe")
    
 
    certificado = criar_certificado_na_bd(session, certificado_schema,instituicao)

    # 1 - gerar QR localmente
    qr_path = gerar_qr(certificado.hash)

    # 2 - gerar PDF com o QR embutido
    dados_certificado = {
        "nome_aluno": certificado.nome_aluno,
        "curso": certificado.curso,
        "carga_horaria": certificado.carga_horaria,
        "data_emissao": certificado.data_emissao,
        "nome da instituicao":certificado.instituicao.nome,
        
    }
    pdf_path = gerar_pdf_certificado(dados_certificado, qr_path)

    
    pdf_url = local_path_url(pdf_path)
    qr_url = local_path_url(qr_path)

    # 5 - atualizar paths no DB
    certificado = actualizar_caminho(session, certificado.id, pdf_path=pdf_url, qr_path=qr_url)
    return certificado
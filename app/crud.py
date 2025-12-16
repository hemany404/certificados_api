from sqlalchemy.orm import Session
from app.models.modelos import Certificado
from app.schemas.schema import CertificadoSchema
from app.utils.gerar_hash import gerar_hash
from app.models.modelos import Instituicao

def criar_certificado_na_bd(session: Session, certificado_schema: CertificadoSchema,instituicao:Instituicao):
    dados = {
        "nome_aluno":certificado_schema.nome_aluno,
        "curso":certificado_schema.curso,
        "carga_horaria":certificado_schema.carga_horaria,
        "data_emissao":certificado_schema.data_emissao,
    }
    codigo =gerar_hash(dados)
    certificado = Certificado(
        nome_aluno=certificado_schema.nome_aluno,
        curso=certificado_schema.curso,
        carga_horaria=certificado_schema.carga_horaria,
        data_emissao=certificado_schema.data_emissao,
        instituicao_id=instituicao.id,
        hash = codigo
    )
    session.add(certificado)
    session.commit()
    session.refresh(certificado)
    return certificado

def obter_certificado_pelo_hash(session: Session, codigo_hash: str):
    return session.query(Certificado).filter(Certificado.hash == codigo_hash).first()

def actualizar_caminho(session: Session, certificado_id: int, pdf_caminho: str = None, qr_caminho: str = None):
    certificado = session.query(Certificado).get(certificado_id)
    if not certificado:
        return None
    if pdf_caminho:
        certificado.pdf_url = pdf_caminho
    if qr_caminho:
        certificado.qr_url = qr_caminho
    session.commit()
    session.refresh(certificado)
    return certificado

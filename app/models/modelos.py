from sqlalchemy import Integer,Column,String,Date,ForeignKey,DateTime
from sqlalchemy.orm import relationship,declarative_base
from datetime import datetime,timedelta,timezone


Base = declarative_base()

class Instituicao(Base):
    __tablename__ = "instituicoes"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True)
    senha = Column(String, nullable=False)
    logo_url = Column(String,nullable=True)
    criado_em = Column(DateTime, default=datetime.now(timezone.utc))
    
    def __init__(self,nome,email,senha,logo_url):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.logo_url =logo_url


class Certificado(Base):
    __tablename__ = "certificados"

    id = Column(Integer, primary_key=True)
    nome_aluno = Column(String, nullable=False)
    curso = Column(String, nullable=False)
    carga_horaria = Column(Integer, nullable=False)

    data_emissao = Column(Date, nullable=False)

    hash = Column(String, unique=True)
    qrcode_url = Column(String)
    pdf_url = Column(String)

    instituicao_id = Column(Integer, ForeignKey("instituicoes.id"))
    instituicao = relationship("Instituicao")

    criado_em = Column(DateTime, default=datetime.now(timezone.utc))
    

    def __init__(self,nome_aluno,curso,carga_horaria,data_emissao,instituicao_id):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.carga_horaria = carga_horaria
        self.data_emissao = data_emissao
        self.instituicao_id =instituicao_id
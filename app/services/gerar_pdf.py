from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from app.core.config import PDF_FOLDER
from app.utils.gerar_hash import directorio
import os
from PIL import Image

directorio(PDF_FOLDER)

def gerar_pdf_certificado(dados_certificado: dict, qr_path: str) -> str:
    """
    dados_certificado: dict com nome_aluno, curso, emissor, issued_at, codigo_hash
    qr_path: caminho do png do QR
    Retorna path do PDF gerado.
    """
    filename = f"certificado_{dados_certificado['hash']}.pdf"
    out_path = os.path.join(PDF_FOLDER, filename)

    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4

    # Titutlo / Emissor
    y = height - 40*mm
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, y, dados_certificado.get("nome da instituicao"))

    # Certificate title
    y -= 15*mm
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, y, "Certificado de Conclusão")

    # Student name
    y -= 20*mm
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, y, dados_certificado["nome_aluno"])

    # Course
    y -= 10*mm
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, y, f"Concluiu o curso: {dados_certificado['curso']}")

    # Issued
    y -= 12*mm
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, y, f"Emitido em: {dados_certificado['data_emissao']}")

    # QR (lower-right)
    if qr_path and os.path.exists(qr_path):
        qr_img = Image.open(qr_path)
        qr_w = 40*mm
        qr_h = 40*mm
        qr_tmp = qr_path
        c.drawImage(qr_tmp, width - 60*mm, 30*mm, qr_w, qr_h)

   

    c.showPage()
    c.save()
    return out_path

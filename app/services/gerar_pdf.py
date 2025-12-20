from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from app.core.config import PDF_FOLDER
from app.utils.gerar_hash import directorio
import os
from PIL import Image

directorio(PDF_FOLDER)

def gerar_pdf_certificado(dados_certificado: dict, qr_caminho: str) -> str:
   
    nome_pdf = f"certificado_{dados_certificado['nome_aluno']}.pdf"
    pdf = os.path.join(PDF_FOLDER, nome_pdf)

    c = canvas.Canvas(pdf, pagesize=A4)
    width, height = A4

   
    y = height - 40*mm
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2, y, dados_certificado.get("nome da instituicao"))

 
    y -= 15*mm
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, y, "Certificado de Conclusão")

    
    y -= 20*mm
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, y, dados_certificado["nome_aluno"])

    
    y -= 10*mm
    c.setFont("Helvetica", 14)
    c.drawCentredString(width/2, y, f"Concluiu o curso: {dados_certificado['curso']}")
    
    c.setFont("Helvetica", 12)
    c.drawCentredString(
        width / 2,
        height - 125 * mm,
        f"Carga horária: {dados_certificado['carga_horaria']} horas"
    )
    
    y -= 12*mm
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, y, f"Emitido em: {dados_certificado['data_emissao']}")

    
    if qr_caminho and os.path.exists(qr_caminho):
        qr_img = Image.open(qr_caminho)
        qr_w = 40*mm
        qr_h = 40*mm
        qr_tmp = qr_caminho
        c.drawImage(qr_tmp, width - 60*mm, 30*mm, qr_w, qr_h)

 

    c.showPage()
    c.save()
    return pdf

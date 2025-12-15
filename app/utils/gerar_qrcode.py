import qrcode
from PIL import Image
from io import BytesIO
from app.core.config import QR_FOLDER, BASE_URL
from app.utils.gerar_hash import directorio
import os

directorio(QR_FOLDER)

def gerar_qr(codigo_hash: str, tamanho=290) -> str:
    """
    Gera QR que aponta para o endpoint público de verificação:
    {BASE_URL}/verificar/{codigo_hash}
    Salva arquivo local e retorna caminho relativo absoluto.
    """
    url = f"{BASE_URL}/verificar/{codigo_hash}"
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    nome_qr = f"qr_{codigo_hash}.png"
    path = os.path.join(QR_FOLDER, nome_qr)
    img.save(path)
    return path

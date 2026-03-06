from PIL import Image
import numpy as np
from crypto import gerar_chave, criptografar, descriptografar


delimitador = "#####"


def texto_para_binario(texto):
    texto = texto + delimitador

    binarios = [format(ord(letra), '08b') for letra in texto]

    binarios_juntos = "".join(binarios)

    return binarios_juntos


def binario_para_texto(binario):
    texto = ""
    n = 8
    slicing = [binario[i:i+n] for i in range(0, len(binario), n)]

    for i in slicing:
        if len(i) == 8:
            numero = int(i, 2)
            letra = chr(numero)
            texto += letra

    if delimitador in texto:
        texto = texto.split(delimitador)[0]

    return texto


def hide_msg(image, texto_criptografado):
    image = Image.open(image)
    pixels = np.array(image)
    formato_original = pixels.shape
    binario = texto_para_binario(texto_criptografado)

    if pixels.size < len(binario):
        raise ValueError("The image is too small to hide message")

    pixels = pixels.flatten()

    for i in range(len(binario)):
        bit = int(binario[i])
        pixel_atual = pixels[i]
        pixel_atualizado = (pixel_atual & 254) | bit
        pixels[i] = pixel_atualizado

    pixels = pixels.reshape(formato_original)

    image_with_msg = Image.fromarray(pixels.astype(np.uint8))

    return image_with_msg


def reveal_msg(image_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    pixels = pixels.flatten()

    bits = "".join((pixels & 1).astype(str))

    texto_criptografado = binario_para_texto(bits)

    return texto_criptografado

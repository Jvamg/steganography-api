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


if __name__ == "__main__":
    segredo = "O cofre ta atras do quadro"

    print(f"1. Mensagem Original: {segredo}")

    binario = texto_para_binario(segredo)
    print(f"2. Tripa Binária (vai pros pixels): {binario}")

    revelado = binario_para_texto(binario)
    print(f"3. Mensagem Revelada: {revelado}")

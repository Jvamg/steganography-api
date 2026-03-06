from cryptography.fernet import Fernet


def gerar_chave():
    chave = Fernet.generate_key()
    return chave


def criptografar(texto, chave):
    f = Fernet(chave)
    texto_criptografado = f.encrypt(texto.encode()).decode()
    return texto_criptografado


def descriptografar(texto_criptografado, chave):
    f = Fernet(chave)
    texto = f.decrypt(texto_criptografado.encode()).decode()
    return texto

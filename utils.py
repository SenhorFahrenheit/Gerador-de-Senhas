import random
import string

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase  # letras minúsculas
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase  # letras maiúsculas
    if incluir_numeros:
        caracteres += string.digits  # números
    if incluir_simbolos:
        caracteres += string.punctuation  # símbolos

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

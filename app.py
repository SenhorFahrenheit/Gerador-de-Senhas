from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    senha = None  # Inicializa a variável senha

    if request.method == "POST":
        senha = gerar()  # Chama a função gerar e armazena a senha gerada
    
    return render_template('index.html', senha=senha)

def gerar():
    tamanho = int(request.form.get('tamanho', 12))  # Padrão de 12 caracteres
    incluir_maiusculas = 'maiusculas' in request.form
    incluir_numeros = 'numeros' in request.form
    incluir_simbolos = 'simbolos' in request.form
    
    senha = gerar_senha(tamanho, incluir_maiusculas, incluir_numeros, incluir_simbolos)
    return senha

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase  # letras minúsculas
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase  # letras maiúsculas
    if incluir_numeros:
        caracteres += string.digits  # números
    if incluir_simbolos:
        caracteres += string.punctuation  # símbolos

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

if __name__ == '__main__':
    app.run(debug=True)

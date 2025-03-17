from flask import Flask, render_template, request
from utils import gerar_senha  

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    senha = None  # Inicializa a variável senha

    if request.method == "POST":
        tamanho = int(request.form.get('tamanho', 12))  # Padrão de 12 caracteres
        incluir_maiusculas = 'maiusculas' in request.form
        incluir_numeros = 'numeros' in request.form
        incluir_simbolos = 'simbolos' in request.form

        senha = gerar_senha(tamanho, incluir_maiusculas, incluir_numeros, incluir_simbolos)

    return render_template('index.html', senha=senha)

if __name__ == '__main__':
    app.run(debug=True)

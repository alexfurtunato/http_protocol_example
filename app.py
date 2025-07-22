from flask import Flask, render_template, request, jsonify
from datetime import datetime, date

app = Flask(__name__)

pessoas_ficticias = [
    {"nome": "João Silva", "data_nascimento": "1990-05-15"},
    {"nome": "Maria Santos", "data_nascimento": "1985-12-22"},
    {"nome": "Pedro Oliveira", "data_nascimento": "1992-08-10"},
    {"nome": "Ana Costa", "data_nascimento": "1988-03-07"},
    {"nome": "Carlos Souza", "data_nascimento": "1995-11-30"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
    p_f = [{"nome": p["nome"], "data_nascimento": date.fromisoformat(p["data_nascimento"]).strftime("%d/%m/%Y")} for p in pessoas_ficticias]
    return jsonify(p_f)

@app.route('/calcular-idade', methods=['POST'])
def calcular_idade():
    data_nascimento = request.form['data_nascimento']
    
    try:
        nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
        hoje = date.today()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        
        return render_template('resultado.html', idade=idade, data_nascimento=data_nascimento)
    except ValueError:
        return render_template('index.html', erro="Data inválida. Use o formato AAAA-MM-DD")

@app.route('/teste500', methods=['GET'])
def forcar_erro():
    # Forçando um erro 500 para teste
    return pessoas_ficticias[100]

if __name__ == '__main__':
    app.run(debug=True)
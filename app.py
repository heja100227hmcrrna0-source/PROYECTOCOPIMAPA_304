import webbrowser
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/validar', methods=['POST'])
def validar():

    usuario = request.form['usuario']
    password = request.form['password']

    if usuario.lower().endswith('copimapa') and password == '21102026':
        return redirect('/menu')

    return render_template(
    'error.html',
    mensaje='El usuario debe terminar en COPIMAPA y la contraseña debe ser correcta.'
)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/lugares')
def lugares():
    return render_template('lugares.html')

@app.route('/sugerencias')
def sugerencias():
    return render_template('sugerencias.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/integrantes')
def integrantes():
    return render_template('integrantes.html')

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
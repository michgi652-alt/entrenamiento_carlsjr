from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    return redirect(url_for('inicio'))

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/evaluaciones')
def evaluaciones():
    return render_template('evaluaciones.html')

if __name__ == '__main__':
    app.run(debug=True)
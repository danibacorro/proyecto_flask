from flask import Flask, render_template, request
import json

app = Flask(__name__)	

with open('pruebas_coches.json', encoding='utf-8') as f:
    coches_json = json.load(f)


@app.route('/')
def inicio():
    return render_template("index.html")

@app.route("/busqueda")
def busqueda():
    return render_template("busqueda.html")

@app.route('/lista', methods=['POST'])
def lista():
    listado = []
    nombre = request.form.get('buscador', '').lower()
    for coche in coches_json:
        for prueba in coche["pruebas"]:
            if nombre in prueba["modelo"].lower() or nombre == '':
                listado.append({
                    "id": prueba["id"],
                    "modelo": prueba["modelo"],
                    "consumo_combinado": prueba["consumo"]["combinado"]
                })
    return render_template('lista.html', listado=listado)

if __name__ == "__main__":
    app.run()

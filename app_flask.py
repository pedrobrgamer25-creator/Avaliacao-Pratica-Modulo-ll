from flask import Flask, request, render_template, jsonify 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma", methods=['GET'])
def get_soma():
     valor1 = float(request.args.get("valor1"))
     valor2 = float(request.args.get("valor2"))
     resultado = valor1 + valor2
     return jsonify ({"Resultado:", resultado})

@app.route("/subtrair", methods=['GET'])
def get_subtrair():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    resultado = valor1 - valor2
    return jsonify ({"Resultado:", resultado})

@app.route("/multiplicar", methods=['GET'])
def get_multiplicar():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    resultado = valor1 * valor2
    return jsonify ({"Resultado:", resultado})

@app.route("/dividir", methods=['GET'])
def get_dividir():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    resultado = valor1 / valor2
    return jsonify ({"Resultado:", resultado})
    if v2 == 0:
        return {"erro": "Divisão por zero não é permitida"}
## Continue o código aqui.

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request

from ExamenFinalGrupal01 import clasificar_cuadrilatero, validar_datos

app = Flask(__name__)

LADOS = ["a", "b", "c", "d"]
ANGULOS = ["A", "B", "C", "D"]


def procesar(valores):
    try:
        numeros = [float(valores[k]) for k in LADOS + ANGULOS]
    except (KeyError, TypeError, ValueError):
        return {"ok": False, "errores": ["Error: completa todos los campos con números."]}

    validos, errores = validar_datos(*numeros)
    if not validos:
        return {"ok": False, "errores": errores}

    resultado, explicacion = clasificar_cuadrilatero(*numeros)
    return {"ok": True, "resultado": resultado, "explicacion": explicacion}


@app.route("/", methods=["GET", "POST"])
def index():
    valores = request.form.to_dict() if request.method == "POST" else {}
    respuesta = procesar(valores) if request.method == "POST" else {}
    return render_template(
        "index.html",
        lados=LADOS,
        angulos=ANGULOS,
        valores=valores,
        errores=respuesta.get("errores"),
        resultado=respuesta.get("resultado"),
        explicacion=respuesta.get("explicacion"),
    )


@app.post("/api/clasificar")
def api_clasificar():
    return jsonify(procesar(request.get_json(silent=True) or {}))


if __name__ == "__main__":
    app.run(debug=True)

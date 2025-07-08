from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
from flask_cors import CORS
import numpy as np
import os

app = Flask(__name__)
CORS(app)  

modelo_path = "modelo_gato.h5"
model = load_model(modelo_path)

def preparar_imagen(imagen):
    imagen = imagen.resize((150, 150)).convert("RGB")
    array = np.array(imagen) / 255.0
    return np.expand_dims(array, axis=0)

@app.route("/predict", methods=["POST"])
def predecir():
    if "imagen" not in request.files:
        return jsonify({"error": "No se encontró el archivo 'imagen'"}), 400

    archivo = request.files["imagen"]
    imagen = Image.open(archivo)
    preparada = preparar_imagen(imagen)
    pred = model.predict(preparada)[0][0]

    return jsonify({
        "gato": bool(pred < 0.5),
        "confianza": float(pred)
    })

@app.route("/")
def index():
    return "Backend Flask funcionando"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

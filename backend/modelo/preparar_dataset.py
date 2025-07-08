#Se corre una sola vez para separar las imagenes de gatos y perros del dataset
import os
import shutil

base_origen = "dogs-vs-cats/train"
base_destino = "dataset"

os.makedirs(f"{base_destino}/gato", exist_ok=True)
os.makedirs(f"{base_destino}/no_gato", exist_ok=True)

for archivo in os.listdir(base_origen):
    if archivo.startswith("cat"):
        shutil.copy(os.path.join(base_origen, archivo), os.path.join(base_destino, "gato", archivo))
    elif archivo.startswith("dog"):
        shutil.copy(os.path.join(base_origen, archivo), os.path.join(base_destino, "no_gato", archivo))

print("✅ Dataset preparado con éxito en: backend/modelo/dataset/")

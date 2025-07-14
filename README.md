# Reconocimiento de Gatos
Este proyecto es un sistema web que detecta si una imagen contiene un gato o no, usando:
-TensorFlow (modelo entrenado)
-Flask (API backend)
-React (frontend)

## Cómo usar
1. Cloná el repositorio en `https://github.com/ValentinoVerdi/reconocimiento-gatos`
2. Descargá el modelo: `modelo_gato.h5` en `https://drive.google.com/file/d/1rAbEmxjxu1fJ7THEbcur-EzgYnQ9w1hh/view?usp=drive_link`
2. Pegá el archivo `modelo_gato.h5` en `backend/modelo`
4. Instalá dependencias en `backend/` y `frontend/` con `npm install`
5. Entrená el modelo con `python3 entrenar.py` 
6. Corré el backend con `python3 api.py`
7. Corré el frontend con `npm run dev`
8. Subí una imagen y verificá si es un gato

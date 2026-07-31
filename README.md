# CaféData ☕

Predicción de ventas diarias de un café en Bogotá según la temperatura y la lluvia.

## Instalación y ejecución

```bash
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/train.py
```

## Estructura

```
cafedata/
├── data/               # Datos crudos (no se versionan en proyectos reales)
│   └── cafe_ventas.csv
├── src/
│   ├── data.py         # Carga y validación de datos
│   └── train.py        # Entrenamiento y evaluación
├── tests/
├── requirements.txt    # Dependencias con versiones fijadas
└── README.md
```

"""Entrenamiento del modelo de CaféData."""
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from data import cargar_datos, separar_variables

import pandas as pd

def entrenar():
    df = cargar_datos()
    X, y = separar_variables(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X_test)
    mae = mean_absolute_error(y_test, predicciones)

    print(f"Filas de entrenamiento: {len(X_train)}")
    print(f"Filas de prueba:        {len(X_test)}")
    print(f"MAE: {mae:.1f} tazas")

    # Predicción de ejemplo: día frío y lluvioso en Bogotá
    
    ejemplo = pd.DataFrame({"temperatura_c": [10.0], "llovio": [1]})
    print(f"Predicción para 10 °C con lluvia: {modelo.predict(ejemplo)[0]:.0f} tazas")

    return modelo


if __name__ == "__main__":
    entrenar()

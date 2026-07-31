"""Carga y preparación de datos para CaféData."""
from pathlib import Path

import pandas as pd

# Ruta relativa a la raíz del proyecto — funciona en cualquier máquina.
RUTA_DATOS = Path(__file__).parent.parent / "data" / "cafe_ventas.csv"


def cargar_datos(ruta: Path = RUTA_DATOS) -> pd.DataFrame:
    """Carga el CSV de ventas y valida lo mínimo."""
    df = pd.read_csv(ruta)

    # El reflejo profesional: verificar tipos apenas se carga.
    columnas_esperadas = {"temperatura_c", "llovio", "ventas_tazas"}
    faltantes = columnas_esperadas - set(df.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas en el CSV: {faltantes}")

    return df


def separar_variables(df: pd.DataFrame):
    """Devuelve (X, y) sin modificar el DataFrame recibido."""
    X = df[["temperatura_c", "llovio"]].copy()
    y = df["ventas_tazas"].copy()
    return X, y

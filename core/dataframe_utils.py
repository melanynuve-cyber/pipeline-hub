# core/dataframe_utils.py
import os
from typing import List, Optional

import pandas as pd


def read_csv_safe(
    file_path: str,
    sep: str = ",",
) -> Optional[pd.DataFrame]:
    # Retorna None si el archivo no existe o falla la lectura
    if not os.path.exists(file_path):
        return None

    try:
        return pd.read_csv(file_path, sep=sep, dtype=str)
    except Exception:
        return None


def is_not_empty(df: Optional[pd.DataFrame]) -> bool:
    # Verifica que el DataFrame exista y tenga registros
    return df is not None and not df.empty


def to_snake_case(df: pd.DataFrame) -> pd.DataFrame:
    # Normaliza encabezados a snake_case
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return df


def drop_columns(
    df: pd.DataFrame,
    cols: List[str],
) -> pd.DataFrame:
    # Elimina columnas indicadas si existen en el DataFrame
    return df.drop(columns=cols, errors="ignore")


def cast_column_types(
    df: pd.DataFrame,
    int_cols: List[str] = [],
    float_cols: List[str] = [],
) -> pd.DataFrame:
    """
    Convierte columnas al tipo numerico indicado.
    Los valores que no se puedan convertir quedan como NaN.
    """
    for col in int_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].round(0)

    for col in float_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

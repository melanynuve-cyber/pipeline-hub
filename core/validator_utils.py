# core/validator_utils.py
import logging
from typing import List, Optional

import pandas as pd

logger = logging.getLogger(__name__)


def validate_required_columns(
    df: pd.DataFrame,
    required_cols: List[str],
) -> bool:
    # Verifica que todas las columnas requeridas existan en el DataFrame
    missing = [col for col in required_cols if col not in df.columns]

    if missing:
        logger.warning("Columnas faltantes: %s", missing)
        return False

    return True


def validate_no_nulls(
    df: pd.DataFrame,
    cols: List[str],
) -> bool:
    # Verifica que las columnas indicadas no tengan valores nulos
    for col in cols:
        if col not in df.columns:
            continue

        null_count = int(df[col].isnull().sum())

        if null_count > 0:
            logger.warning(
                "Columna '%s' tiene %s valores nulos", col, null_count
                )
            return False

    return True


def validate_numeric_range(
    df: pd.DataFrame,
    col: str,
    min_val: Optional[float] = None,
    max_val: Optional[float] = None,
) -> bool:
    """
    Verifica que los valores de una columna numerica
    se encuentren dentro del rango esperado.
    """
    if col not in df.columns:
        logger.warning(
            "Columna '%s' no encontrada para validacion de rango", col
            )
        return False

    series = pd.to_numeric(df[col], errors="coerce").dropna()

    if min_val is not None:
        if int((series < min_val).sum()) > 0:
            logger.warning(
                "Columna '%s' tiene valores menores a %s", col, min_val
                )
            return False

    if max_val is not None:
        if int((series > max_val).sum()) > 0:
            logger.warning(
                "Columna '%s' tiene valores mayores a %s", col, max_val
                )
            return False

    return True


def drop_duplicates(
    df: pd.DataFrame,
    subset: Optional[List[str]] = None,
) -> pd.DataFrame:
    # Elimina filas duplicadas y registra la cantidad removida
    before = len(df)
    df = df.drop_duplicates(subset=subset, keep="first")
    removed = before - len(df)

    if removed > 0:
        logger.warning("Se eliminaron %s filas duplicadas", removed)

    return df

# pipelines/home_rental/transform.py
import logging
from typing import List

import pandas as pd

from core.dataframe_utils import cast_column_types, drop_columns
from core.validator_utils import drop_duplicates
from pipelines.home_rental.pipelineinfo import (PIPELINE_NAME,
                                                INT_COLS,
                                                FLOAT_COLS)
from pipelines.home_rental.transform_brules import add_price_per_sqft

logger = logging.getLogger(__name__)


def start(folders: dict, extracted: List[pd.DataFrame]) -> List[pd.DataFrame]:
    _ = folders

    logger.info("Iniciando transform '%s'", PIPELINE_NAME)

    if not extracted:
        logger.warning("No hay DataFrames para transformar.")
        return []

    transformed: List[pd.DataFrame] = []

    for idx, df in enumerate(extracted):
        logger.info("Transformando DataFrame %s/%s", idx + 1, len(extracted))

        try:
            df_t = df.copy()

            # Convierte columnas al tipo numerico correspondiente
            df_t = cast_column_types(
                df_t, int_cols=INT_COLS, float_cols=FLOAT_COLS
                )

            # Elimina filas duplicadas por property_id
            df_t = drop_duplicates(df_t, subset=["property_id"])

            # Agrega columna calculada de precio por metro cuadrado
            df_t = add_price_per_sqft(df_t)

            # Elimina columna de direccion, no es relevante para el modelo
            df_t = drop_columns(df_t, ["address"])

            transformed.append(df_t)
            logger.info("DataFrame transformado: %s registros", len(df_t))

        except Exception as exc:
            logger.exception(
                "Error transformando DataFrame %s: %s", idx + 1, exc
                )

    logger.info(
        "Transform finalizado. DataFrames transformados: %s", len(transformed)
        )
    return transformed

# pipelines/home_rental/extract_validators.py
import logging

import pandas as pd

from core.validator_utils import (
    validate_required_columns,
    validate_no_nulls,
    validate_numeric_range)
from pipelines.home_rental.pipelineinfo import (REQUIRED_COLS,
                                                FLOAT_COLS,
                                                INT_COLS)

logger = logging.getLogger(__name__)


def validate_dataframe(df: pd.DataFrame) -> bool:
    # Verifica que el archivo tenga la estructura esperada
    if not validate_required_columns(df, REQUIRED_COLS):
        return False

    # Verifica que no haya nulos en columnas requeridas
    if not validate_no_nulls(df, REQUIRED_COLS):
        return False

    # Verifica que size y rent_amount sean valores positivos
    for col in FLOAT_COLS + INT_COLS:
        if not validate_numeric_range(df, col, min_val=0):
            return False

    logger.info("Validacion correcta.")
    return True

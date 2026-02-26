# pipelines/home_rental/extract.py
import logging
from typing import List, Optional

import pandas as pd

from core.dataframe_utils import read_csv_safe, to_snake_case
from core.filesystem_utils import list_input_files
from pipelines.home_rental.extract_validators import validate_dataframe
from pipelines.home_rental.pipelineinfo import PIPELINE_NAME

logger = logging.getLogger(__name__)


def process_file(file_path: str) -> Optional[pd.DataFrame]:
    df = read_csv_safe(file_path)

    if df is None or df.empty:
        return None

    # Normaliza encabezados a snake_case
    df = to_snake_case(df)

    return df


def start(folders: dict) -> List[pd.DataFrame]:
    inbound = folders["inbound"]
    files = list_input_files(inbound)

    logger.info(
        "Iniciando extract '%s'. Archivos: %s", PIPELINE_NAME, len(files)
                )

    outputs: List[pd.DataFrame] = []
    invalid_files: List[str] = []

    for file_path in files:
        df = process_file(file_path)

        if df is None:
            invalid_files.append(file_path)
            logger.warning("Archivo vacio o no legible: %s", file_path)
            continue

        if validate_dataframe(df):
            outputs.append(df)
            logger.info(
                "Archivo validado: %s - %s registros", file_path, len(df)
                )
        else:
            invalid_files.append(file_path)
            logger.error("Archivo no valido: %s", file_path)

    if invalid_files:
        logger.warning("Archivos no validos: %s", len(invalid_files))

    logger.info("Extract finalizado. DataFrames validos: %s", len(outputs))
    return outputs

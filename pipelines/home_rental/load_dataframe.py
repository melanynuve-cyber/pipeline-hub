# pipelines/home_rental/load_dataframe.py
import logging
import os

import pandas as pd

from pipelines.home_rental.pipelineinfo import PIPELINE_NAME

logger = logging.getLogger(__name__)


def prepare_df(
    df: pd.DataFrame,
    output_dir: str,
    idx: int,
) -> None:
    # Construye el nombre del archivo de salida
    file_name = f"{PIPELINE_NAME}_{idx + 1}.csv"
    file_path = os.path.join(output_dir, file_name)

    # Guarda el DataFrame como CSV sin el indice de pandas
    df.to_csv(file_path, index=False)
    logger.info("Archivo guardado: %s", file_path)

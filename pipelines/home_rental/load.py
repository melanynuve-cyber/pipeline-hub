# pipelines/home_rental/load.py
import logging
from typing import List

import pandas as pd

from core.filesystem_utils import move_to_processed
from pipelines.home_rental.load_dataframe import prepare_df
from pipelines.home_rental.pipelineinfo import PIPELINE_NAME

logger = logging.getLogger(__name__)


def start(
    folders: dict,
    transformed: List[pd.DataFrame],
) -> bool:
    logger.info("Iniciando load '%s'", PIPELINE_NAME)

    if not transformed:
        logger.warning("No hay datos para cargar.")
        return False

    output_dir = folders["output"]
    inbound_dir = folders["inbound"]
    processed_dir = folders["processed"]

    try:
        for idx, df in enumerate(transformed):
            logger.info(
                "Guardando DataFrame %s/%s",
                idx + 1,
                len(transformed),
            )

            # Prepara y guarda el DataFrame como CSV
            prepare_df(df, output_dir, idx)

        # Mueve los archivos procesados a historial
        moved = move_to_processed(inbound_dir, processed_dir)
        logger.info("Archivos movidos a processed: %s", moved)

    except Exception as exc:
        logger.exception("Error en LOAD: %s", exc)
        return False

    logger.info("Load '%s' finalizado correctamente.", PIPELINE_NAME)
    return True

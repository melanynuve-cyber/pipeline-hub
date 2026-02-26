# pipelines/pipelines.py
import logging

from pipelines.home_rental import pipeline as home_rental_pipeline

logger = logging.getLogger(__name__)

# Lista de pipelines registrados para ejecucion secuencial
pipelines_list = [
    home_rental_pipeline,
]


def start() -> None:
    logger.info("Iniciando ejecucion de pipelines.")

    for pipeline in pipelines_list:
        try:
            pipeline.start()
        except Exception as exc:
            logger.exception(
                "Error ejecutando pipeline: %s", exc
            )

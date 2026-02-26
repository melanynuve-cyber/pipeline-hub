# core/pipeline_runner.py
import logging
from typing import Callable, List, Optional

import pandas as pd

from core.filesystem_utils import ensure_folders

ExtractFn = Callable[..., List[pd.DataFrame]]
TransformFn = Callable[..., List[pd.DataFrame]]
LoadFn = Callable[..., bool]


def run_pipeline(
    *,
    pipeline_name: str,
    extract_fn: ExtractFn,
    transform_fn: TransformFn,
    load_fn: LoadFn,
    logger: Optional[logging.Logger] = None,
) -> bool:
    log = logger or logging.getLogger(__name__)
    log.info("Iniciando pipeline: %s", pipeline_name)

    # Asegura que las carpetas del pipeline existan antes de ejecutar
    folders = ensure_folders(pipeline_name)
    log.info("Inbound: %s", folders["inbound"])
    log.info("Output: %s", folders["output"])

    # Ejecuta la fase de extraccion
    try:
        extracted: List[pd.DataFrame] = extract_fn(folders=folders)
    except Exception as exc:
        log.exception("Error en EXTRACT: %s", exc)
        return False

    if not extracted:
        log.info("No hay archivos para procesar en %s", folders["inbound"])
        return True

    # Ejecuta la fase de transformacion
    try:
        transformed: List[pd.DataFrame] = transform_fn(
            folders=folders,
            extracted=extracted,
        )
    except Exception as exc:
        log.exception("Error en TRANSFORM: %s", exc)
        return False

    if not transformed:
        log.error("TRANSFORM no produjo resultados.")
        return False

    # Ejecuta la fase de carga
    try:
        result: bool = load_fn(
            folders=folders,
            transformed=transformed,
        )
    except Exception as exc:
        log.exception("Error en LOAD: %s", exc)
        return False

    if not result:
        log.error("LOAD finalizo con errores.")
        return False

    log.info("Pipeline %s finalizado correctamente.", pipeline_name)
    return True

# core/filesystem_utils.py
import logging
import os
import shutil
from datetime import datetime
from typing import List, Optional

logger = logging.getLogger(__name__)


def ensure_folders(pipeline_name: str) -> dict:
    # Crea y asegura la estructura minima de carpetas del pipeline.
    # Retorna las rutas para que el pipeline las pueda usar.
    from core.settings import PIPELINES_DIR

    pipeline_root = os.path.join(PIPELINES_DIR, pipeline_name)
    inbound_dir = os.path.join(pipeline_root, "inbound")
    processed_dir = os.path.join(pipeline_root, "processed")
    output_dir = os.path.join(pipeline_root, "output")

    # Crea las carpetas si no existen
    os.makedirs(inbound_dir, exist_ok=True)
    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    return {
        "pipeline_root": pipeline_root,
        "inbound":       inbound_dir,
        "processed":     processed_dir,
        "output":        output_dir,
    }


def list_input_files(
    inbound_folder: str,
    input_files: Optional[List[str]] = None,
) -> List[str]:
    # Obtiene la lista de archivos CSV a procesar desde inbound.
    # Usa input_files si se proporciona, de lo contrario lista todos los CSV.
    if input_files:
        return [
            os.path.join(inbound_folder, f)
            for f in input_files
        ]

    # Si no, buscamos todos los CSV que esten en la carpeta
    return [
        os.path.join(inbound_folder, f)
        for f in os.listdir(inbound_folder)
        if f.lower().endswith(".csv")
    ]


def move_to_processed(
    source_dir: str,
    processed_dir: str,
) -> int:
    # Mueve los CSV procesados desde inbound a processed,
    # dentro de una subcarpeta con timestamp para tener historial.
    if not os.path.exists(source_dir):
        return 0

    csv_files = [
        os.path.join(source_dir, f)
        for f in os.listdir(source_dir)
        if f.lower().endswith(".csv")
    ]

    if not csv_files:
        logger.info("No hay CSV en inbound para mover a processed.")
        return 0

    # Subcarpeta destino con fecha y hora para no sobreescribir
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    target_dir = os.path.join(processed_dir, stamp)
    os.makedirs(target_dir, exist_ok=True)

    moved = 0
    for src in csv_files:
        dst = os.path.join(target_dir, os.path.basename(src))
        try:
            shutil.move(src, dst)
            moved += 1
        except Exception:
            logger.exception("No se pudo mover %s a %s", src, dst)

    logger.info("Se movieron %s archivos a processed/%s", moved, stamp)
    return moved

# pipelines/home_rental/pipeline.py
import logging

from core.pipeline_runner import run_pipeline
from pipelines.home_rental.extract import start as extract_start
from pipelines.home_rental.transform import start as transform_start
from pipelines.home_rental.load import start as load_start
from pipelines.home_rental.pipelineinfo import PIPELINE_NAME

logger = logging.getLogger(__name__)


def start() -> bool:
    return run_pipeline(
        pipeline_name=PIPELINE_NAME,
        extract_fn=extract_start,
        transform_fn=transform_start,
        load_fn=load_start,
        logger=logger,
    )

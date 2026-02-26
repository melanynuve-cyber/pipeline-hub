# main.py
import logging

from pipelines.pipelines import start as pipelines_start

logger = logging.getLogger(__name__)


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def main() -> None:
    configure_logging()
    logger.info("Iniciando pipeline-hub.")

    try:
        pipelines_start()
    except KeyboardInterrupt:
        logger.info("Ejecucion detenida manualmente.")
    except Exception as exc:
        logger.exception("Error inesperado: %s", exc)

    logger.info("pipeline-hub finalizado.")


if __name__ == "__main__":
    main()

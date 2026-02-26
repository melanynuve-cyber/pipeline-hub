# core/settings.py
import os

# Ruta base del proyecto (carpeta raiz de pipeline-hub)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carpeta donde viven los pipelines
PIPELINES_DIR = os.path.join(BASE_DIR, "pipelines")

# Carpeta donde se guardan los logs de ejecucion
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

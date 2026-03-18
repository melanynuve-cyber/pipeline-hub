**ETL Pipeline Framework**
Este proyecto es un robusto motor de procesamiento de datos Extract, Transform, and Load (ETL) diseñado para gestionar múltiples pipelines de forma modular y escalable. Permite la ingesta de datos, validación de reglas de negocio y carga de resultados con un sistema de reportes automático.

**Estructura del Proyecto**
```
.
├── main.py                 # Punto de entrada principal
├── core/                   # Utilerías globales y motor del framework
│   ├── pipeline_runner.py  # Orquestador central (Extract → Transform → Load)
│   ├── settings.py         # Configuraciones y rutas base
│   └── *_utils.py          # Helpers de filesystem, validación y dataframes
├── pipelines/              # Módulos de procesamiento específicos
│   ├── pipelines.py        # Despachador de pipelines
│   ├── home_rental/        # Pipeline 1: Predicción de renta
│   ├── diabetes/           # Pipeline 2: Clasificación de diabetes
│   ├── ice_cream/          # Pipeline 3: Predicción de ventas
│   └── penguins/           # Pipeline 4: Clasificación de pingüinos
└── reports/                # Logs y métricas de ejecución (Auto-generados)
```

**Componentes por Pipeline**
Cada pipeline (ej. home_rental, diabetes) sigue una arquitectura interna estandarizada:

inbound/: Carpeta para archivos CSV recibidos y pendientes de procesar.

processed/: Histórico de archivos ya procesados con marca de tiempo.

output/: Resultados finales tras la transformación y carga.

extract.py & extract_validators.py: Lógica de extracción y limpieza inicial.

transform.py & transform_brules.py: Aplicación de reglas de negocio (Business Rules).

load.py & load_dataframe.py: Destino final de los datos procesados.

**Cómo empezar**
Requisitos
Asegúrate de tener Python instalado y las dependencias necesarias:
```
pip install pandas
```
Ejecución
Para correr el motor y procesar los datos, simplemente ejecuta el archivo principal:
```
python main.py
```
**Flujo de Datos**
Extract: El sistema busca archivos en inbound/ y valida su integridad.
Transform: Se aplican filtros y reglas lógicas definidas en transform_brules.py.
Load: El resultado se guarda en output/ y el origen se mueve a processed/.
Report: Se genera un log detallado en la carpeta reports/.

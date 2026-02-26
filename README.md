# ETL

FLUJO ESPERADO
ETL/
│
├── main.py                          # Punto de entrada, corre los pipelines
│
├── core/                            # Utilerías globales compartidas
│   ├── pipeline_runner.py           # Motor que orquesta Extract→Transform→Load
│   ├── dataframe_utils.py           # Helpers para leer y manipular DataFrames
│   ├── filesystem_utils.py          # Manejo de carpetas y archivos
│   ├── settings.py                  # Rutas base del proyecto
│   └── validator_utils.py           # Validaciones genéricas de datos
│
├── pipelines/                       # Aquí vive cada pipeline
│   ├── pipelines.py                 # Despachador (decide qué pipeline correr)
│   │
│   ├── home_rental/                 # Pipeline 1 — Predicción de renta
│   │   ├── inbound/                 # CSVs pendientes de procesar
│   │   ├── processed/               # CSVs ya procesados (con timestamp)
│   │   ├── output/                  # Resultado final en CSV
│   │   ├── pipeline.py              # Orquestador del flujo
│   │   ├── pipelineinfo.py          # Nombre, columnas y configuración local
│   │   ├── extract.py
│   │   ├── extract_validators.py
│   │   ├── transform.py
│   │   ├── transform_brules.py
│   │   ├── load.py
│   │   └── load_dataframe.py
│   │
│   ├── diabetes/                    # Pipeline 2 — Clasificación de diabetes
│   │   ├── inbound/
│   │   ├── processed/
│   │   ├── output/
│   │   ├── pipeline.py
│   │   ├── pipelineinfo.py
│   │   ├── extract.py
│   │   ├── extract_validators.py
│   │   ├── transform.py
│   │   ├── transform_brules.py
│   │   ├── load.py
│   │   └── load_dataframe.py
│   │
│   ├── ice_cream/                   # Pipeline 3 — Predicción de ventas
│   │   ├── inbound/
│   │   ├── processed/
│   │   ├── output/
│   │   ├── pipeline.py
│   │   ├── pipelineinfo.py
│   │   ├── extract.py
│   │   ├── extract_validators.py
│   │   ├── transform.py
│   │   ├── transform_brules.py
│   │   ├── load.py
│   │   └── load_dataframe.py
│   │
│   └── penguins/                    # Pipeline 4 — Clasificación de pingüinos
│       ├── inbound/
│       ├── processed/
│       ├── output/
│       ├── pipeline.py
│       ├── pipelineinfo.py
│       ├── extract.py
│       ├── extract_validators.py
│       ├── transform.py
│       ├── transform_brules.py
│       ├── load.py
│       └── load_dataframe.py
│
└── reports/                         # Logs de cada ejecución
    └── (se generan automáticamente)
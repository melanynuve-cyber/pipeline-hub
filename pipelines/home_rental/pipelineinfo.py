# pipelines/home_rental/pipelineinfo.py

PIPELINE_NAME = "home_rental"

# Columnas esperadas en el archivo fuente
REQUIRED_COLS = [
    "property_id", "address",
    "postal_code", "size",
    "bedrooms", "rent_amount"
    ]

# Columnas numericas enteras
INT_COLS = ["property_id", "postal_code", "bedrooms"]

# Columnas numericas decimales
FLOAT_COLS = ["size", "rent_amount"]

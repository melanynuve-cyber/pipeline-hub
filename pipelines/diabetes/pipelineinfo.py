# pipelines/diabetes/pipelineinfo.py

PIPELINE_NAME = "diabetes"

# Columnas esperadas en el archivo fuente
REQUIRED_COLS = [
    "patient_id",
    "pregnancies",
    "plasma_glucose",
    "diastolic_blood_pressure",
    "triceps_thickness",
    "serum_insulin",
    "bmi",
    "diabetes_pedigree",
    "age",
    "diabetic",
]

# Columnas numericas enteras
INT_COLS = [
    "patient_id",
    "pregnancies",
    "plasma_glucose",
    "diastolic_blood_pressure",
    "triceps_thickness",
    "serum_insulin",
    "age",
    "diabetic",
]

# Columnas numericas decimales
FLOAT_COLS = [
    "bmi",
    "diabetes_pedigree",
]

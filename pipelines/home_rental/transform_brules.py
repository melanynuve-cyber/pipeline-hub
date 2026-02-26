# pipelines/home_rental/transform_brules.py
import logging

import pandas as pd

logger = logging.getLogger(__name__)


def add_price_per_sqft(df: pd.DataFrame) -> pd.DataFrame:
    # Calcula el precio por pie cuadrado de cada propiedad
    df["price_per_sqft"] = (
        df["rent_amount"] / df["size"]
    ).round(2)

    return df

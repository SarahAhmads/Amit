import pandas as pd
import numpy as np
from check_dtype import check_dtype
def handle_types(df, cols):
    df[cols] = df[cols].astype('category')
    check_dtype(df)
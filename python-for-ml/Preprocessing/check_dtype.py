import pandas as pd
import numpy as np

def check_dtype(df):
    dtypes = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({'Dtypes': dtypes, 'num_unique': n_unique}).T
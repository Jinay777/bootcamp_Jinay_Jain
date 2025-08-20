import pandas as pd
import numpy as np

def fill_missing_median(df, columns=None):
    """
    Fill missing values with median for specified columns.
    """
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=[np.number]).columns.tolist()
    for col in columns:
        out[col] = out[col].fillna(out[col].median())
    return out

def drop_missing(df, axis=0, how='any', subset=None):
    """
    Drop rows or columns with missing values.
    """
    return df.dropna(axis=axis, how=how, subset=subset)

def normalize_data(df, columns=None, method='zscore'):
    """
    Normalize numeric columns using z-score or min-max.
    """
    out = df.copy()
    if columns is None:
        columns = out.select_dtypes(include=[np.number]).columns.tolist()
    for col in columns:
        if method == 'zscore':
            out[col] = (out[col] - out[col].mean()) / out[col].std()
        elif method == 'minmax':
            out[col] = (out[col] - out[col].min()) / (out[col].max() - out[col].min())
        else:
            raise ValueError("method must be 'zscore' or 'minmax'")
    return out

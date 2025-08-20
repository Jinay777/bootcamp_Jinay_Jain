import pandas as pd
import numpy as np
from pathlib import Path
import sys
import os

# Add project root to sys.path
sys.path.append(r"D:/bootcamp_Jinay_Jain/homework/homework6")  # raw string for Windows

# Create folders if not exist
Path("../data/raw").mkdir(parents=True, exist_ok=True)
Path("../data/processed").mkdir(parents=True, exist_ok=True)

# Generate financial raw dataset
dates = pd.date_range(start="2024-01-01", periods=100, freq="B")
np.random.seed(42)
open_prices = np.random.uniform(100, 200, 100)
close_prices = open_prices + np.random.uniform(-5, 5, 100)
high_prices = np.maximum(open_prices, close_prices) + np.random.uniform(0, 5, 100)
low_prices = np.minimum(open_prices, close_prices) - np.random.uniform(0, 5, 100)
volumes = np.random.randint(100000, 1000000, 100)

df_raw = pd.DataFrame({
    "Date": dates,
    "Open": open_prices.round(2),
    "High": high_prices.round(2),
    "Low": low_prices.round(2),
    "Close": close_prices.round(2),
    "Volume": volumes
})

# Introduce missing values
for col in ["Open", "High", "Low", "Close", "Volume"]:
    df_raw.loc[df_raw.sample(frac=0.1).index, col] = np.nan

# Save raw data
raw_path = Path("homework/homework6/data/raw/financial_raw.csv")
df_raw.to_csv(raw_path, index=False)

# Import cleaning functions
from src.cleaning import fill_missing_median, drop_missing, normalize_data

# Load raw data
df_raw = pd.read_csv(raw_path)

# Clean numeric columns
numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
df_filled = fill_missing_median(df_raw, columns=numeric_cols)
df_dropped = drop_missing(df_filled)
df_cleaned = normalize_data(df_dropped, columns=numeric_cols, method='zscore')

# Save cleaned data
processed_path = Path("homework/homework6/data/processed/cleaned_dataset.csv")
df_cleaned.to_csv(processed_path, index=False)

# Compare
print("Original Dataset Shape:", df_raw.shape)
print("Cleaned Dataset Shape:", df_cleaned.shape)
print("\nMissing Values Before Cleaning:\n", df_raw.isnull().sum())
print("\nMissing Values After Cleaning:\n", df_cleaned.isnull().sum())
print("\nOriginal Summary:")
print(df_raw.describe())
print("\nCleaned Summary:")
print(df_cleaned.describe())

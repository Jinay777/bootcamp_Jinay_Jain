## Data Cleaning Strategy for Financial Dataset

- **Raw Data:** `data/raw/financial_raw.csv`
- **Processed Data:** `data/processed/financial_cleaned.csv`

### Steps:
1. **Fill Missing Values:** Replaced NaN with median for numeric columns.
2. **Drop Missing:** Removed rows with any remaining NaNs.
3. **Normalization:** Applied Z-score scaling to numeric columns.
4. **Assumptions:**
   - Non-numeric column (`Date`) not normalized.
   - Median chosen to handle outliers.
5. **Output:** Cleaned dataset ready for further analysis or modeling.

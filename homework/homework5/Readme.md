## Data Storage

### Folder Structure
- `data/raw/` → original CSV files
- `data/processed/` → processed Parquet files

### Formats Used
- **CSV**: human-readable, easy to inspect, compatible with most tools.
- **Parquet**: efficient, compressed columnar format, better for large datasets.

### Environment Variables
- `DATA_DIR_RAW` → points to `data/raw/`
- `DATA_DIR_PROCESSED` → points to `data/processed/`

The code reads/writes files using these env variables, e.g.:

```python
from dotenv import load_dotenv
import os
import pathlib

load_dotenv()
RAW = pathlib.Path(os.getenv("DATA_DIR_RAW", "data/raw"))
PROC = pathlib.Path(os.getenv("DATA_DIR_PROCESSED", "data/processed"))

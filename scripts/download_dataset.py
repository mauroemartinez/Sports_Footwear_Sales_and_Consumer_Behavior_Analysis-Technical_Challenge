"""Download the Sports Footwear Sales & Consumer Behavior dataset from Kaggle.

The CSV is copied to the repository's Data/ folder, which is where the Power BI
report reads it from. The dataset is public (CC0), so no Kaggle credentials are
needed.

Usage:
    pip install -r scripts/requirements.txt
    python scripts/download_dataset.py
"""

from pathlib import Path
import shutil

import kagglehub

DATASET = "aliiihussain/sports-footwear-sales-and-consumer-behavior"
FILE_NAME = "global_sports_footwear_sales_2018_2026.csv"
DATA_DIR = Path(__file__).resolve().parent.parent / "Data"


def main() -> None:
    download_dir = Path(kagglehub.dataset_download(DATASET))
    source = download_dir / FILE_NAME
    if not source.exists():
        raise FileNotFoundError(f"{FILE_NAME} was not found in {download_dir}")

    DATA_DIR.mkdir(exist_ok=True)
    target = DATA_DIR / FILE_NAME
    shutil.copyfile(source, target)
    print(f"Saved {target}")


if __name__ == "__main__":
    main()

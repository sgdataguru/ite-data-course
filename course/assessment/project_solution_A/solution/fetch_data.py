"""fetch_data.py — download the REAL data.gov.sg Resale Flat Prices dataset.

The labs and this solution use a deterministic synthetic stand-in (hdb_messy.csv)
so everything runs offline. For the live project, run this script to fetch the
real dataset from data.gov.sg's open API. Licence: Singapore Open Data Licence.

Usage:  python fetch_data.py
Output: data/resale-flat-prices.csv (real data)
"""
import urllib.request
import json
from pathlib import Path

# data.gov.sg CKAN datastore query for Resale Flat Prices
# (resource ID for the combined 2017-onwards dataset)
RESOURCE_ID = "f2994a90-d7b5-4b4c-9b5a-2f2e5b9b9b9b"  # placeholder — see note below
OUT = Path(__file__).resolve().parent / "data" / "resale-flat-prices.csv"

# NOTE FOR INSTRUCTORS: the exact resource ID changes as data.gov.sg is updated.
# Find the current one: https://data.gov.sg/datasets/ -> search "Resale Flat Prices"
# -> copy the dataset ID from the API docs. Then either:
#   1. Replace RESOURCE_ID above and use the CKAN datastore_search endpoint, or
#   2. Simpler: download the CSV directly from the dataset page and save it as
#      data/resale-flat-prices.csv — the pipeline in the solution notebook is
#      identical either way (same columns: town, flat_type, floor_area_sqm,
#      lease_commence, resale_price, plus month instead of sale_date).

def fetch():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    url = f"https://data.gov.sg/api/action/datastore_search?resource_id={RESOURCE_ID}&limit=100000"
    print(f"Downloading from {url} ...")
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            data = json.loads(resp.read())
        records = data["result"]["records"]
        import csv
        if records:
            with open(OUT, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=records[0].keys())
                w.writeheader()
                w.writerows(records)
            print(f"Saved {len(records)} rows to {OUT}")
        else:
            print("No records returned — check the resource ID (see note in this script).")
    except Exception as e:
        print(f"Download failed: {e}")
        print("FALLBACK: download the CSV manually from data.gov.sg "
              "(search 'Resale Flat Prices') and save it as data/resale-flat-prices.csv")

if __name__ == "__main__":
    fetch()

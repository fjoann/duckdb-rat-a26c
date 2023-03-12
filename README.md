# duckdb-rat-a26c

Explore the use of DuckDB from within Python.

## How to use

Download three years worth of trip record data from the [TLC website] (about 13 GB). Automate this
with `curl`:

```
curl -ZO "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_20[20-22]-[01-12].parquet"
```

Create a .env file:

```
# trip record data directory
DATA_DIR=
```

Export the environment variables:

```
set -a
source .env
set +a
```

Build and run a DuckDB development container:

```
make build
make dev
```

Run the Python script:

```
python duckdb_demo/duckdb_demo.py
```

[TLC website]: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

# duckdb-rat-a26c

Explore the use of DuckDB from within Python.

## How to use

Download three years worth of trip record data from the [TLC website][1] (about 13 GB). Automate this
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

## Next steps

Do a test with DuckDB and the Iceberg API on data in S3, similar to what Alon Agmon does in this [blog][2].

[1]: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
[2]: https://towardsdatascience.com/boost-your-cloud-data-applications-with-duckdb-and-iceberg-api-67677666fbd3

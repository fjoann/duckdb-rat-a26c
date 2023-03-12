import duckdb

con = duckdb.connect()

print('Simple row count.')
con.sql("""
    SELECT
        count(*) as rows
    FROM
        '/var/lib/data/*.parquet'
""").show()

print('Group over the entire dataset.')
con.sql("""
    SELECT
        Hvfhs_license_num,
        avg(trip_time) AS trip_time_avg
    FROM
        '/var/lib/data/*.parquet'
    GROUP BY
        Hvfhs_license_num
""").show()

print('Group and order over a subset of the data.')
con.sql("""
    SELECT
        strftime(Pickup_datetime, '%Y%m') as year_month,
        count(*) as trips
    FROM
        '/var/lib/data/*.parquet'
    WHERE
        request_datetime >= strptime('2022-10-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    GROUP BY
        year_month
    ORDER BY
        year_month
""").show()

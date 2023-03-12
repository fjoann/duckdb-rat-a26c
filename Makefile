.PHONY: dev
dev:
	@docker run \
	--rm \
	-it \
	--mount type=bind,source=$(DATA_DIR),target=/var/lib/data \
	--mount type=bind,source=$(CURDIR),target=/app \
	duckdb-rat-a26c:latest

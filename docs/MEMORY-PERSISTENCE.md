# Persistent memory

Set `IAPUTA_MEMORY_DB_PATH` to an absolute writable database path outside the Git checkout. The default remains `iaputa_os_memory.db` for compatibility. The application creates parent directories and initializes the schema.

For Docker, provision a persistent volume at `/app/data` and set `IAPUTA_MEMORY_DB_PATH=/app/data/iaputa_os_memory.db` explicitly. Before recreating a running container, stop writers, create a SQLite-consistent backup of the actual database, verify integrity and restore into the mounted volume. Do not start with an empty replacement if existing data is expected. Preserve the old container and backup until acceptance. No production migration is performed by this PR.

The historical tracked snapshot is recoverable from Git; it is not a backup of live data. Run the persistence regression test with `python -m pytest tests/test_memory_persistence.py`.

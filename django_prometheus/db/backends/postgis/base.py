from django.contrib.gis.db.backends.postgis import base
from django.db.backends.postgresql import base as pg_base

from django_prometheus.db.common import DatabaseWrapperMixin, ExportingCursorWrapper

# PostGIS rides on the PostgreSQL driver; detect v3 vs v2 the same way.
_IS_PSYCOPG3 = getattr(pg_base.Database, "__name__", "") == "psycopg"

if not _IS_PSYCOPG3:
    import psycopg2.extensions


class DatabaseWrapper(DatabaseWrapperMixin, base.DatabaseWrapper):
    def get_connection_params(self):
        conn_params = super().get_connection_params()
        if not _IS_PSYCOPG3:
            conn_params["cursor_factory"] = ExportingCursorWrapper(
                psycopg2.extensions.cursor, "postgis", self.vendor
            )
        return conn_params

    def get_new_connection(self, conn_params):
        connection = super().get_new_connection(conn_params)
        if _IS_PSYCOPG3:
            connection.cursor_factory = ExportingCursorWrapper(
                connection.cursor_factory, "postgis", self.vendor
            )
        return connection

    def create_cursor(self, name=None):
        # cursor_factory is a kwarg to connect() so restore create_cursor()'s
        # default behavior
        return base.DatabaseWrapper.create_cursor(self, name=name)

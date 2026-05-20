from django.contrib.gis.db.backends.postgis import base

from django_prometheus.db.common import DatabaseWrapperMixin, ExportingCursorWrapper

try:
    # psycopg2 (Django's legacy driver); absent under Django 5 + psycopg v3.
    import psycopg2.extensions

    _PSYCOPG2_CURSOR = psycopg2.extensions.cursor
except ImportError:  # psycopg v3 only
    _PSYCOPG2_CURSOR = None


class DatabaseWrapper(DatabaseWrapperMixin, base.DatabaseWrapper):
    def get_connection_params(self):
        conn_params = super().get_connection_params()
        if _PSYCOPG2_CURSOR is not None:
            conn_params["cursor_factory"] = ExportingCursorWrapper(
                _PSYCOPG2_CURSOR, "postgis", self.vendor
            )
        return conn_params

    def create_cursor(self, name=None):
        # cursor_factory is a kwarg to connect() so restore create_cursor()'s
        # default behavior
        return base.DatabaseWrapper.create_cursor(self, name=name)

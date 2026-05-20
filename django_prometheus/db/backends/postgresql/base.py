from django.db.backends.postgresql import base

from django_prometheus.db.common import DatabaseWrapperMixin, ExportingCursorWrapper

# Django binds the active driver module to `base.Database`: `psycopg` for v3
# (the Django 5 default) or `psycopg2` for the legacy driver.
_IS_PSYCOPG3 = getattr(base.Database, "__name__", "") == "psycopg"

if not _IS_PSYCOPG3:
    import psycopg2.extensions


class DatabaseFeatures(base.DatabaseFeatures):
    """Our database has the exact same features as the base one."""

    pass


class DatabaseWrapper(DatabaseWrapperMixin, base.DatabaseWrapper):
    def get_connection_params(self):
        conn_params = super().get_connection_params()
        if not _IS_PSYCOPG3:
            # psycopg2: Django doesn't set a cursor_factory, so inject the
            # metrics-emitting cursor at connection time.
            conn_params["cursor_factory"] = ExportingCursorWrapper(
                psycopg2.extensions.cursor, self.alias, self.vendor
            )
        return conn_params

    def get_new_connection(self, conn_params):
        connection = super().get_new_connection(conn_params)
        if _IS_PSYCOPG3:
            # psycopg v3: Django sets connection.cursor_factory to its own
            # Cursor subclass while opening the connection. Wrap that class so
            # query metrics are emitted while keeping Django's cursor behavior.
            connection.cursor_factory = ExportingCursorWrapper(
                connection.cursor_factory, self.alias, self.vendor
            )
        return connection

    def create_cursor(self, name=None):
        # cursor_factory (set above for both drivers) drives the wrapping, so
        # restore create_cursor()'s default behavior.
        return base.DatabaseWrapper.create_cursor(self, name=name)

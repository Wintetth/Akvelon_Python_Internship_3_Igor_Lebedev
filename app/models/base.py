from peewee import PostgresqlDatabase
from peewee import Model

from app.utilities.database.constants import DATABASE


class Base(Model):
    class Meta:
        database: PostgresqlDatabase = DATABASE
        legacy_table_names: bool = False

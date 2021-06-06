from peewee import PostgresqlDatabase

DATABASE_NAME: str = "finances"
DATABASE: PostgresqlDatabase = PostgresqlDatabase(database=DATABASE_NAME)

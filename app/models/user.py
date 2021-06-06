from peewee import AutoField, TextField

from app.models.base import Base


class User(Base):
    user_id: AutoField = AutoField()

    first_name: TextField = TextField()
    last_name: TextField = TextField(null=True)

    email: TextField = TextField(unique=True)
    password: TextField = TextField()
    
    key: TextField = TextField(unique=True)

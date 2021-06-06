from datetime import date

from peewee import DateField, FloatField, ForeignKeyField, AutoField, Ordering

from app.models.base import Base
from app.models.user import User


class Transaction(Base):
    transaction_id: AutoField = AutoField()
    
    user: ForeignKeyField = ForeignKeyField(User, backref="transactions", on_delete="CASCADE")

    amount: FloatField = FloatField(default=0)
    date: DateField = DateField(default=date.today)
    

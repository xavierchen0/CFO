from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


@dataclass
class Transaction(db.Model):
    transaction_id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False
    )
    date: Mapped[datetime.date] = mapped_column(nullable=False)
    income: Mapped[bool] = mapped_column(nullable=False)
    category_name: Mapped[str] = mapped_column(nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)

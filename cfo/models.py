from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dataclasses import dataclass


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


@dataclass
class Transaction(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    isIncome: Mapped[bool] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)

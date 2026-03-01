from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, MappedAsDataclass

from app_v1.models.database_models.base_model import DatabaseBaseModel


class User(DatabaseBaseModel):
    __tablename__ = 'users' # TODO: create a common registry for all tables
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, init=False)
    user_name: Mapped[str] = mapped_column(String, nullable=False, index=True) # Compulsory
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True) # Compulsory
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), init=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC), init=False)

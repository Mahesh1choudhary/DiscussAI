from datetime import datetime, UTC
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = 'users' # TODO: create a common registry for all tables
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime, default=datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

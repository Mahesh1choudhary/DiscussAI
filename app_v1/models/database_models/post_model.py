from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, JSON, DateTime
from typing import Dict, Any

from app_v1.models.database_models.base_model import DatabaseBaseModel

#TODO: single table will suffice as entry will be in 1000 range only, consider multiple tables or other optimisations later
class Post(DatabaseBaseModel):
    __tablename__ = 'posts' #TODO: store in single registry

    post_id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    post_source: Mapped[str] = mapped_column(String(100), nullable=False)
    post_id_in_source: Mapped[str] = mapped_column(String(100), nullable=False)
    post_link:Mapped[str] = mapped_column(String(1000), nullable=False)

    post_creation_date_in_source: Mapped[datetime] = mapped_column(DateTime, nullable=False, index=True)
    post_type: Mapped[str] = mapped_column(String(100), index=True, nullable=True)
    post_company_name: Mapped[str] = mapped_column(String(100), index=True, nullable=True)
    post_role_name: Mapped[str] = mapped_column(String(100), index=True, nullable=True)

    post_metadata: Mapped[Dict[str, Any]] = mapped_column(JSON, default=dict)




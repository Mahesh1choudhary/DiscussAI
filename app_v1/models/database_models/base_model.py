from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, MappedAsDataclass


class DatabaseBaseModel(MappedAsDataclass, DeclarativeBase):
    pass
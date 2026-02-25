from dataclasses import dataclass
from typing import Dict, Optional


class BaseDBConfig:
    """ Base configurations for DB"""
    backend_db: str  # db configured on backend

    # common db configs- default values
    batch_size: int = 5000
    max_workers: int = 10



@dataclass
class PostgresSQLDBConfig(BaseDBConfig):
    """postgresSQL specific configuration"""
    backend_db: str = "postgressql"
    batch_size: int = 5000
    max_workers: int = 10

    postgresSQL_db_connection_pool_min = 2
    postgresSQL_db_connection_pool_max = 5
    postgresSQL_db_db_name: str = ""
    postgresSQL_db_user: str = ""
    postgresSQL_db_password: str = ""
    postgresSQL_db_host: str = ""
    postgresSQL_db_port: str = ""




class DBConfigFactory:
    """ Factory for creating backend-specific db configurations """

    _config_classes: Dict[str, type] = {
        "postgresSQL": PostgresSQLDBConfig,
    }

    @classmethod
    def create_config(cls, backend_db_name:str) -> BaseDBConfig:
        """ create configuration for the specific backend db"""
        if backend_db_name not in cls._config_classes:
            available_backend_dbs = ", ".join(cls._config_classes.keys())
            raise ValueError(f"Unknown backend db name: {backend_db_name}. Available backends: {available_backend_dbs}")

        #TODO: get the data from config and create config




class DBConfigManager:
    """Manager for DB configurations"""

    def __init__(self):
        self._config = Optional[BaseDBConfig] = None

    def get_config(self) -> BaseDBConfig:
        if self._config is None:
            #TODO: fetch from config and then create_config in configfactory
            return BaseDBConfig()






global_db_config_manager = DBConfigManager()


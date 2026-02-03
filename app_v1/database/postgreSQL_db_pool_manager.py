import threading

from app_v1.global_services import global_db_config_manager
from app_v1.database.db_config import PostgreSQLDBConfig


class BaseDBPoolManager:
    """

    """
    _instance = None
    _initialised = False
    _lock = threading.Lock() # lock for initialization
    _connection_pool = None # all connections

    _prepared_connections = {} # connections that are prepared or ready
    _prepared_connections_lock = threading.Lock()  # to protect race conditions on _prepared_connections

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(BaseDBPoolManager, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        if not self._initialised:
            with self._lock:
                if not self._initialised:
                    self._initialise_connection_pool()
                    self._initialised = True


    def _initialise_connection_pool(self):
        """ to initialise number of connections as per the config"""
        raise NotImplementedError("Subclasses must implement initialise_connection_pool method.")

    def _prewarm_connection_pool(self):
        """ to prepare and establish some connections with basic settings"""
        raise NotImplementedError("Subclasses must implement _prewarm_connection_pool method.")


    def get_connection(self):
        """ to get a connection from the pool"""
        raise NotImplementedError("Subclasses must implement get_connection method.")

    def release_connection(self):
        """ to release the connection to the pool"""
        raise NotImplementedError("Subclasses must implement release_connection method.")




class PostgreSQLDbPoolManager(BaseDBPoolManager):

    _instance = None
    _initialised = False
    _lock = threading.Lock() # lock for initialization
    _connection_pool = None # all connections

    _prepared_connections = {} # connections that are prepared or ready
    _prepared_connections_lock = threading.Lock()  # to protect race conditions on _prepared_connections

    def _initialise_connection_pool(self):
        try:
            db_config = global_db_config_manager.get_config()
            if not isinstance(db_config, PostgreSQLDBConfig):
                raise TypeError("Expected db_config: {}, but got {}".format(PostgreSQLDBConfig.__name__, type(db_config).__name__))

        except Exception as e:
            raise RuntimeError("Error")




import threading
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseManager():
    _lock = threading.Lock()
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        with self._lock:
            if getattr(self, "_initialised", False):
                return

            self._initialised = True
            database_url = "test"
            self.engine = create_engine(
                database_url,
                pool_size = 10,
                max_overflow = 20,
                pool_pre_ping = True,
                pool_recycle = 3600,
            )

            self.session_local = sessionmaker(
                bind = self.engine,
                autocommit = False,
                autoflush = False,
            )

    def get_session(self):
        return self.session_local()


database_manager = DatabaseManager()


def get_database_session():
    session = database_manager.get_session()
    try:
        yield session
    finally:
        session.close()


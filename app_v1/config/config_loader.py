from typing import Union
from enum import Enum
import os, sys, yaml

from pydantic.v1 import ConfigError
from app.config.config_keys import EnvironmentConfigKeys

_CONFIG = {}  # currently for local development only. config_cache is already implemented as per future key-value store migration


def load_config():
    global _CONFIG
    if _CONFIG is not None:
        return _CONFIG

    env_type = os.getenv(EnvironmentConfigKeys.ENV.value, "local")
    config_file_path = f"app/config/local_config/{env_type}_config.yaml"

    if not os.path.exists(config_file_path):
        error_msg = f"config file for ENV:'{env_type}' not found at {config_file_path}."
        raise ConfigError(error_msg)

    data = {}
    with open(config_file_path, "r") as config_file:
        data = yaml.safe_load(config_file) or {}

    _CONFIG = data
    return _CONFIG


def fetch_key_value(key: Union[str, Enum]):
    if isinstance(key, Enum):
        key = key.value

    config = load_config()
    if not hasattr(config, key):
        error_msg = f"Key:'{key}' not found in local config file"
        raise KeyError(error_msg)

    return getattr(config, key)

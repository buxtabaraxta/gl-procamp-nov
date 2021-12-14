from config_simple.base_config import BaseConfig
import os

from config_simple.provider import (
    ConfigFromSimpleJsonProvider,
)


# Parent class inheritanse
class Config(BaseConfig):
    DEFAULT_ENV = "prod"

    # constructor
    def __init__(self) -> None:
        # hasmap for java
        self.conf_dict = {}

        json_config_path = (
            f"config_simple/predefined/{os.environ.get('TARGET', self.DEFAULT_ENV)}.json"
        )

        self.config_provider = ConfigFromSimpleJsonProvider(json_config_path)

        # call constructor of superclass/parentclass
        super(Config, self).__init__()

        self._register("BASE_URL")
        self._register("GRID_HUB_URL")
        self._register("SOME_VAR_YOU_DO_NOT_NEED")


# Pythonic way of singleton pattern
CONFIG = Config()

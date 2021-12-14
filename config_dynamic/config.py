from config_dynamic.base_config import BaseConfig
import os

from config_dynamic.provider import (
    ConfigFromDictProvider,
    ConfigFromEnvProvider,
    ConfigFromSimpleJsonProvider,
    HierarchicalProvider,
)


# Parent class inheritanse
class Config(BaseConfig):
    DEFAULT_ENV = "prod"

    # constructor
    def __init__(self) -> None:
        # hasmap for java
        self.conf_dict = {}

        json_config_path = (
            f"config_dynamic/predefined/{os.environ.get('TARGET', self.DEFAULT_ENV)}.json"
        )

        app_env = ConfigFromEnvProvider()
        app_json_conf = ConfigFromSimpleJsonProvider(json_config_path)
        app_defaults = ConfigFromDictProvider(
            {
                "GRID_HUB_URL": "http://selenium-grid:4444/wd/hub",
                "BASE_URL": "DICT"
            }
        )
        self.config_provider = HierarchicalProvider(
            [app_env, app_json_conf, app_defaults]
        )

        # call constructor of superclass/parentclass
        super(Config, self).__init__()

        self._register("BASE_URL")
        self._register("GRID_HUB_URL")
        self._register("SOME_VAR_YOU_DO_NOT_NEED")


# Pythonic way of singleton pattern
CONFIG = Config()

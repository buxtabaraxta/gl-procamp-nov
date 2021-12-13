from config.base_config import BaseConfig
import os

from config.provider import (
    ConfigFromDictProvider,
    ConfigFromEnvProvider,
    ConfigFromSimpleJsonProvider,
    HierarchicalProvider,
)


class Config(BaseConfig):
    DEFAULT_ENV = "prod"

    def __init__(self) -> None:
        config_path = (
            f"config/predefined/{os.environ.get('TARGET', self.DEFAULT_ENV)}.json"
        )

        app_env = ConfigFromEnvProvider()
        app_json_conf = ConfigFromSimpleJsonProvider(config_path)
        app_defaults = ConfigFromDictProvider(
            {
                "GRID_HUB_URL": "http://selenium-grid:4444/wd/hub",
            }
        )
        self.config_provider = HierarchicalProvider(
            [app_env, app_json_conf, app_defaults]
        )

        super(Config, self).__init__()
        self._register("BASE_URL")
        self._register("GRID_HUB_URL")


CONFIG = Config()

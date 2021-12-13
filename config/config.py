
from config.provider import ConfigFromDictProvider, ConfigFromEnvProvider, ConfigFromSimpleJsonProvider, HierarchicalProvider
import os


class Config():
    def __init__(self) -> None:
        self.conf_dict = {}
        
        config_path = f"config/predefined/{os.environ['TARGET']}.json"

        app_env = ConfigFromEnvProvider()
        app_json_conf = ConfigFromSimpleJsonProvider(config_path)
        app_defaults = ConfigFromDictProvider(
            {
                "GRID_HUB_URL": "http://selenium-grid.dev.cosmosid.com:4444/wd/hub",
            }
        )
        super(Config, self).__init__()
        self.config_provider = HierarchicalProvider([app_env, app_json_conf, app_defaults])

        self._register('BASE_URL')
        self._register('GRID_HUB_URL')

    def _register(self, item):
        self.conf_dict[item] = self.config_provider.get(item)

    def __getattr__(self, item):
        if item in self.conf_dict:
            return self.conf_dict[item]
        raise AttributeError()


CONFIG = Config()

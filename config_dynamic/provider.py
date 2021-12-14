import os
import json


class BaseConfigKeyProvider(object):
    """
    Base class for config providers,
    should not be used directly
    """
    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """
        raise NotImplementedError("Not implemented")


class ConfigFromEnvProvider(BaseConfigKeyProvider):
    """
    Allows configuration through the env variables.
    """
    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """
        val = os.environ.get(key)
        return val


class ConfigFromDictProvider(BaseConfigKeyProvider):
    """
    Allows configuration through the simple dict object
    """
    def __init__(self, config):
        """
        :param dict config: Configuration dict
        """
        if config is None:
            raise ValueError("Config parameter is mandatory")
        # thread safe deep copy
        self.config = json.loads(json.dumps(config))

    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """
        val = self.config.get(key)
        return val


class ConfigFromSimpleJsonProvider(BaseConfigKeyProvider):
    """
    Allows configuration through the JSON file
    """
    def __init__(self, config_path):
        """
        :param config_path: path to the json with configuration
        """
        self._config_data = ConfigFromSimpleJsonProvider._read_config(config_path)

    @staticmethod
    def _read_config(config_path):
        with open(config_path) as json_file:
            return json.load(json_file)

    def get(self, key):
        """
        Returns config value for the given key
        :param str key: Key to retrieve
        """
        val = self._config_data.get(key)
        return val


class HierarchicalProvider(BaseConfigKeyProvider):
    """
    Allows to create hierarchical override model,
    for ex:
    1. Env config (most priority)
    2. Json config (less priority)
    3. Dict config (with defaults)

    In this situation the get key will try tio return value from 1st,
    in case it not configured (None) => resolve from 2nd,
    in case it not configured from the last one in the passed list
    """
    def __init__(self, providers=None):
        """
        :param providers: Single item or list of ConfigKeyProvider subclass
        """
        self.providers = providers

    def get(self, key):
        """
        Returns not None key value from the 1st best provider
        or None if nothing configured
        :param str key: Key to retrieve
        """
        for provider in self.providers:
            result = provider.get(key)
            if result is not None:
                return result
        return None

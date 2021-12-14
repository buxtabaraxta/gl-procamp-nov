class BaseConfig:
    def __init__(self) -> None:
        self.conf_dict = {}

    def _register(self, item):
        self.conf_dict[item] = self.config_provider.get(item)

    # python way
    def __getattr__(self, item):
        if item in self.conf_dict:
            return self.conf_dict[item]
        raise AttributeError("Please register var before usage")

    # Java way: overide of class property getter
    def get(self, item):
        if item in self.conf_dict:
            return self.conf_dict[item]
        raise AttributeError("Please register var before usage")

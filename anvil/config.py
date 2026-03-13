from .versions import VERSIONS
from .errors import UnknownVersionId, UnknownConfigSetting
class Config:
    def __setitem__(self, config_key, config_value):
        if config_key == "version":
            if not isinstance(config_value, VERSIONS):
                raise UnknownVersionId(f"Version '{config_value}' is not instance of {VERSIONS}")

            
            self.version = config_value
            print(f"Neue Version gesetzt: {self.version}")
            return

        raise UnknownConfigSetting(f"config '{config_key}' not found")
    

    def __getitem__(self, config_key):
        if config_key == "version":
            return self.version

        raise UnknownConfigSetting(f"config '{config_key}' not found")

        
config = Config()

# default is 21w43a
#config.version = VERSIONS.VERSION_21W43A
config.version = VERSIONS.VERSION_21W43A
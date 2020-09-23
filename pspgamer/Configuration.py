import yaml
import logging


class Configuration:
    def __init__(self):
        self.log = logging.getLogger("ConfManager")
        conf_file = "./default.yaml"
        self.log.info(f"Loading file {conf_file}")

        with open(conf_file) as file:
            self.conf = yaml.load(file, Loader=yaml.Loader)

    def as_dict(self):
        return self.conf

"""
Setup configuration
"""

import os
import io
import logging
from typing import List
from configparser import ConfigParser, ExtendedInterpolation

logger = logging.getLogger(__name__)


class EnvironmentInterpolation(ExtendedInterpolation):

    def before_get(self, parser, section, option, value, defaults):
        # environment varialbes
        value = os.path.expandvars(value)
        # config file variables
        value = super().before_get(parser, section, option, value, defaults)
        return value


class RichConfigParser(ConfigParser):

    def __init__(self):
        super().__init__(self, interpolation=EnvironmentInterpolation())

    def __str__(self):
        text = io.StringIO()
        for section in self.sections():
            text.write(f"[{section}]\n")
            for (key, value) in self.items(section):
                text.write(f"{key}={value}\n")
        return text.getvalue()

    def get_list(self, section, option) -> List[str]:
        value = self.get(section, option)
        return produce_list(value)


def produce_list(text:str) -> List[str]:
        result = text.splitlines()
        result = map(str.strip, result)
        result = filter(None, result)
        return list(result)


def ensure_environment() -> None:
    """
    Provide environment variables expected by 'config.ini'
    """
    if not os.environ.get('HOME'):
        os.environ['HOME'] = '/root'
    if not os.environ.get('PWD'):
        os.environ['PWD'] = os.getcwd()


def produce_config() -> RichConfigParser:
    """
    Setup configuration
    """
    ensure_environment()
    config_parser = RichConfigParser()
    config_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(config_dir, "config.ini")
    config_parser.read(config_path)
    config_path_list = config_parser.get_list('config', 'path_list')
    logger.debug(f"Using config_path_list: {config_path_list}")
    config_parser.read(config_path_list)
    return config_parser


CONFIG = produce_config()

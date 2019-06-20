import logging
from devrepo.config import CONFIG

logging.basicConfig(
    level=CONFIG['logging']['level'].strip().upper(),
    datefmt=CONFIG['logging']['datefmt'].strip(),
    format=CONFIG['logging']['format'].strip(),
)

from devrepo.register import *
from devrepo.shell import *

__all__ = [
    'register_repository',
    'base_dir',
    'shell',
]

"""
Repository manager
"""

import os
import sys
import inspect
import logging

from devrepo.config import CONFIG

logger = logging.getLogger(__name__)


def env_get(name: str) -> str:
    return os.environ.get(name, None)


def env_set(name: str, value: str) -> None:
    os.environ[name] = value


class PythonPath():
    """
    Inject project source during development
    """

    python_key = 'PYTHONPATH'

    @staticmethod
    def value() -> str:
        return env_get(PythonPath.python_key)

    @staticmethod
    def inject_source(project_source:str) -> None:
        logger.info(f"inject_source: {project_source}")
        PythonPath.inject_enviro_source(project_source)
        PythonPath.inject_syspath_source(project_source)

    @staticmethod
    def inject_enviro_source(project_source:str) -> None:
        python_path = env_get(PythonPath.python_key)
        if python_path and not project_source in python_path:
            python_path = f"{project_source}:{python_path}"
        else:
            python_path = f"{project_source}"
        env_set(PythonPath.python_key, python_path)

    @staticmethod
    def inject_syspath_source(project_source:str) -> None:
        if not project_source in sys.path:
            sys.path.insert(0, project_source)


def register_repository():
    """
    Register development repository packages
    """

    this_stack = inspect.stack()
    caller_info = this_stack[1]
    caller_file = caller_info[1]
    caller_path = os.path.abspath(caller_file)

    logger.info(f"register_repository: caller_path: {caller_path}")

    source_list = CONFIG.get_list('layout', 'source_list')

    for source in source_list:
        if source in caller_path:
            project_root = caller_path.split(source)[0]
            for source in source_list:
                project_source = f"{project_root}{source}"
                PythonPath.inject_source(project_source)

    logger.info(f"register_repository: env_path: {PythonPath.value()}")
    logger.info(f"register_repository: sys_path: {sys.path}")

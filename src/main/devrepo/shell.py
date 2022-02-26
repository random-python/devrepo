import os
import shutil
import inspect
import logging
import subprocess
from typing import List

from devrepo.config import CONFIG

logger = logging.getLogger(__name__)


def find_root_by_test_list(path:str, test_list:List[str]) -> str:
    if not path:
        return None
    base = os.path.dirname(path)
    if base == path:
        return None
    for test in test_list:
        test_path = base + os.sep + test
        if os.path.isdir(test_path):
            return base
    return find_root_by_test_list(base, test_list)


def discover_entry_path() -> str:
    """
    Discover tool script
    """
    this_stack = inspect.stack()
    script_file = this_stack[0].filename
    script_path = os.path.abspath(script_file)
    return script_path


def base_dir(with_path:str=''):
    """
    Discover project root
    """
    scm_list = CONFIG.get_list('layout', 'scm_list')
    source_list = CONFIG.get_list('layout', 'source_list')
    test_list = scm_list + source_list
    entry_path = discover_entry_path()
    project_root = find_root_by_test_list(entry_path, test_list)
    if project_root:
        folder = os.path.abspath(f"{project_root}/{with_path}")
        return folder
    else:
        raise RuntimeError(f"Missing project root: {entry_path}")


def shell(script:str) -> None:
    """
    Invoke shell inside project root
    """
    logger.info(f"shell('{script}')")
    program = shutil.which(CONFIG['shell']['program'])
    command = [program, '-c', script]
    project_root = base_dir()
    subprocess.check_call(command, cwd=project_root)

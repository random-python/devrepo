
import os
import sys
import inspect

from devrepo import shell
from devrepo.shell import base_dir
from devrepo.shell import find_root_by_test_list


def test_stack():
    print()
    # print(f"sys.argv[0]={sys.argv[0]}")
    stack = inspect.stack()
    for info in stack:
        print(info)

# def test_entry_path():
#     print()
#     start_path = os.path.abspath(__file__)
#     entry_path = discover_entry_path()
#     print(f"start_path={start_path}")
#     print(f"entry_path={entry_path}")


def test_find_root():
    print()
    dir_list = ['/git/objects']
    testing_path = os.path.abspath(__file__)
    print(f"testing_path={testing_path}")
    project_root = find_root_by_test_list(testing_path, dir_list)
    print(f"project_root={project_root}")


def test_shell():
    print()
    shell("pwd; ls -las")


def test_project_dir():
    print()
    folder = base_dir()
    print(folder)
    folder = base_dir('hello/kitty')
    print(folder)
    folder = base_dir('../../.')
    print(folder)

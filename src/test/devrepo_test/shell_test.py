
from devrepo.shell import *


def test_stack():
    print()
    stack = inspect.stack()
    for info in stack:
        print(info)


def test_find_root():
    print()
    dir_list = ['/src/test']
    testing_path = os.path.abspath(__file__)
    project_root = find_root_by_test_list(testing_path, dir_list)
    print(f"project_root={project_root}")


def xxx_test_shell():
    print()
    shell("pwd; ls -las")


def xxx_test_project_dir():
    print()
    folder = base_dir()
    print(folder)
    folder = base_dir('hello/kitty')
    print(folder)
    folder = base_dir('../../.')
    print(folder)

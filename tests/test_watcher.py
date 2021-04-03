from simple_dir_watcher.watcher import create_command_string


def test_create_command_string():
    assert create_command_string(["pytest", "."]) == "pytest ."
    assert create_command_string(["pytest", "something"]) == "pytest something"

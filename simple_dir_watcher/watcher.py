import os
import time
from typing import Union, Iterable

from watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer

IGNORE_REGEXES = [r'.*\.pytest_cache.*', r'.*__pycache__.*']
SLEEP_BETWEEN_POLLS = 1


def create_command_string(arguments: Union[str, Iterable[str]]) -> str:
    return " ".join(arguments) if isinstance(arguments, list) else arguments


def get_current_directory() -> str:
    return os.path.abspath(os.curdir)


def watcher_workflow(arguments: Union[str, Iterable[str]], ignore_regexes: Iterable[str]):
    events = []
    command = create_command_string(arguments)
    source_change_handler = RegexMatchingEventHandler(ignore_directories=True, ignore_regexes=ignore_regexes)
    source_change_handler.on_any_event = lambda e: events.append(e)
    path = get_current_directory()
    source_observer = Observer()
    source_observer.schedule(source_change_handler, path, recursive=True)
    source_observer.start()

    try:
        while True:
            time.sleep(SLEEP_BETWEEN_POLLS)
            if events:
                print("Events found, executing command...", events)
                events.clear()
                os.system(command)
    except KeyboardInterrupt:
        source_observer.stop()
    source_observer.join()

import sys

from simple_dir_watcher.watcher import watcher_workflow, IGNORE_REGEXES


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    watcher_workflow(args, IGNORE_REGEXES)

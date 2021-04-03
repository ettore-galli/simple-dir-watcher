import sys

from simple_dir_watcher.watcher import watcher_workflow, IGNORE_REGEXES

if __name__ == "__main__":
    watcher_workflow(sys.argv[1:], IGNORE_REGEXES)

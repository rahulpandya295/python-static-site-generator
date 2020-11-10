from os import mkdir
from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest #+ "/" + Path(self.source).relative_to(path)
        mkdir(directory, True, True)

    def build(self):
        mkdir(self.dest, True, True)
        for path in self.source.rgblob("*"):
            if Path(path).is_dir():
                self.create_dir(path)
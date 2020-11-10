import re
from typing import Dict
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = Content.load(fm, Loader = "FullLoader")
        return cls(metadata, content)
    
    def __init__(self, metadata: Dict, content):
        self.data = metadata
        self.data["content"] = content 
    
    @property
    def body(self):
        return self.data["content"]
     
    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None
    
    @type.setter
    def type(self, type):
        self.data["type"] = type
    
    def __getitem__(self, key):
        return self.data.__getitem__(key)
    
    def __iter__(self):
        return self.data.__iter__()
    
    def __len__(self) -> int: return len(self.data)

    def __repr__(self) -> str:
        data = {}
        for key, value in self.data.items():
            if key != "content":
                data[key] = value 
        return str(data)
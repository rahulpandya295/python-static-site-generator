import re
from typing import Dict
from yaml import Loader, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, Loader):
        _, fm, content = Content.__regex.split(Loader, 2)
        Content.load(fm, Loader = "FullLoader")
        instance = cls()
    
    def __init__(self, metadata: Dict, content):
        self.data = metadata
        self.data.update({"content": content})
    
    @property
    def body(self):
        return self.data["content"]
    
    @property
    def type(self):
        self.data["type"] if "type" in self.data else None
    
    @type.setter
    def type(self, value):
        self.data["type"] = value
    
    def __getitem__(self, k):
        return self.data[k]
    
    def __iter__(self):
        return self.data.__iter__()
    
    def __len__(self) -> int: self.data.__len__()

    def __repr__(self) -> str:
        data = {}
        for (key, value) in self.data.items():
            if key != "content":
                data[key] = value 
        return str(data)
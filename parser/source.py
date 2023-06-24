from typing import Any
from dataclasses import dataclass

@dataclass
class Source:
    id: str = "unknown"
    name: str = "Unknown"
    url: str = None
    md5: str = None

    @staticmethod
    def from_dict(obj: Any) -> 'Source':
        _id = str(obj.get("id"))
        _name = str(obj.get("name"))
        _url = str(obj.get("url"))
        _md5 = str(obj.get("md5"))
        return Source(_id, _name, _url, _md5)

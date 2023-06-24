from dataclasses import dataclass
from enum import Enum
from pygame import Vector3
from hashlib import md5
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Waypoint import Waypoint
    from .WaypointFile import WaypointFile

def vectorStr(v: Vector3):
    if v is None: return ""
    return f"{v.x} {v.y} {v.z}"

class WaypointType(Enum):
    STAND = "stand"
    CROUCH = "crouch"
    PRONE = "prone"
    CLIMB = "climb"

zeroVector = Vector3(0, 0, 0)

@dataclass
class Waypoint:
    _index: int
    file: 'WaypointFile'
    position: Vector3
    type: WaypointType
    angle: Vector3
    unknown: str
    connections: list['Waypoint']
    uuid: str = None

    def __lt__(self, other:'Waypoint'):
        return self.distance_to_first() < other.distance_to_first()
    def __gt__(self, other:'Waypoint'):
        return self.distance_to_first() > other.distance_to_first()
    def __compare__(self, other:'Waypoint') -> bool:
        return self.uuid == other.uuid

    def index(self) -> int:
        if hasattr(self, 'file'):
            return self.file.waypoints.index(self)

    def __init__(self, index:int, position:Vector3, connections:list['Waypoint'], type:WaypointType, angle:Vector3, unknown:str, file:'WaypointFile'):
        self._index = index
        self.position = position
        self.connections = connections
        self.connections.sort()
        self.type = type
        self.angle = angle
        self.unknown = unknown
        self.uuid = md5(str(self).encode('utf-8')).hexdigest()
        self.file = file

    def __repr__(self, connections=False) -> str:
        return f"Waypoint(uuid={self.uuid}, _i={self._index}, i={self.index()}, pos={self.position}, conns={self.connections_str() if connections else len(self.connections)}, type={self.type.name}, angle={self.angle}, ?={self.unknown})"

    def distance_to_zero(self) -> float: return self.position.distance_to(zeroVector)
    def distance_to_first(self) -> float: return self.distance_to(self.file.waypoints[0])
    def distance_to_last(self) -> float: return self.distance_to(self.file.waypoints[-1])
    def distance_to(self, other:'Waypoint') -> float: return self.position.distance_to(other.position)

    def connections_str(self) -> str:
        if len(self.connections) and isinstance(self.connections[0], Waypoint):
            return ' '.join([c.uuid for c in self.connections])
        return ' '.join([str(c) for c in self.connections])

    @staticmethod
    def from_row(index:int, row:list[str], file:'WaypointFile'):
        pos = Vector3([float(p) for p in row[0].split(' ')])
        angle = Vector3([float(p) for p in row[3].split(' ')]) if row[3] else None
        connections = [int(c) for c in row[1].split(' ')] if row[1] else []
        return Waypoint(index, pos, connections, WaypointType(row[2]), angle, row[5], file)
    
    def to_row(self):
        connections = ' '.join([str(c._index) for c in self.connections])
        return ",\t\t\t".join([vectorStr(self.position), connections, self.type.value, vectorStr(self.angle), self.unknown,""])
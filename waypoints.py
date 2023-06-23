# from csv import reader
from dataclasses import dataclass
from pathlib import Path
from enum import Enum, auto
from pprint import pprint
from pygame import Vector3
from tabulate import tabulate
from os import linesep

def vectorStr(v: Vector3):
    return f"{v.x} {v.y} {v.z}"

class WaypointType(Enum):
    STAND = "stand"
    CROUCH = "crouch"
    PRONE = "prone"

@dataclass
class Waypoint:
    index: int
    position: Vector3
    connections: list[int]
    type: WaypointType
    angle: Vector3
    unknown: str

    def __init__(self, index:int, position:Vector3, connections:list[int], type:WaypointType, angle:Vector3, unknown:str):
        self.index = index
        self.position = position
        self.connections = connections
        self.type = type
        self.angle = angle
        self.unknown = unknown        

    def __repr__(self) -> str:
        return f"Waypoint({self.index}, {self.position}, {self.connections}, {self.type}, {self.angle}, {self.unknown})"

    @staticmethod
    def from_row(index:int, row:list[str]):
        pos = Vector3([float(p) for p in row[0].split(' ')])
        angle = Vector3([float(p) for p in row[3].split(' ')])
        connections = [int(c) for c in row[1].split(' ')]
        return Waypoint(index, pos, connections, WaypointType(row[2]), angle, row[5])
    
    def to_row(self):
        connections = ' '.join([str(c) for c in self.connections])
        return ",\t\t\t".join([vectorStr(self.position), connections, self.type.value, vectorStr(self.angle), self.unknown,""])

@dataclass
class WaypointList:
    waypoints: list[Waypoint]
    def __init__(self, waypoints: list[Waypoint]):
        self.waypoints = waypoints

@dataclass  
class WaypointFile:
    path: Path
    rows: list[str]
    waypoints: list[Waypoint]

    def __init__(self, path: Path):
        if (not path is type(Path)): path = Path(path)
        self.path = path
        self.waypoints = self.load()

    def check(self, fix:bool=False):
        for waypoint in self.waypoints:
            for connection in waypoint.connections:
                if connection > len(self.waypoints):
                    print(f"{waypoint} connection {connection} is over {len(self.waypoints)}")
                    if fix: waypoint.connections.remove(connection)
                elif connection < 0:
                    print(f"{waypoint} connection {connection} is under zero")
                    if fix: waypoint.connections.remove(connection)
            if len(waypoint.connections) < 1:
                print(f"{waypoint} has no connections")

    def load(self):
        self.rows = []
        self.waypoints = []
        with self.path.open(newline='') as csvfile:
            rows = csvfile.readlines() # reader(csvfile, skipinitialspace=True, delimiter=' ', quotechar='|')
            for i, row in enumerate(rows):
                if not "," in row: continue
                parts = row.split(',')
                if len(parts) > 6 or len(parts) < 6: raise Exception(f"[{i}] Invalid row length: {len(parts)}")
                row = [r.strip() for r in parts]
                self.rows.append(row)
                self.waypoints.append(Waypoint.from_row(i, row))
        print(f"Loaded {len(self.waypoints)} waypoints from {self.path}")
        return self.waypoints
    
    def save(self, path:Path=None):
        if path is None: path = self.path
        if (not path is type(Path)): path = Path(path)
        with path.open('w', newline='') as csvfile:
            csvfile.write(f"{len(self.waypoints)}\n")
            csvfile.writelines(map(lambda x:x+linesep, [wp.to_row() for wp in self.waypoints]))
        print(f"Wrote {len(self.waypoints)} waypoints to {path}")


file = WaypointFile(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\gulag_wp.csv")

# for waypoint in file.waypoints:
#     print(file.rows[waypoint.index-1])
#     print(waypoint.to_row())

file.check(True)
file.save(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\gulag_wp_fixed.csv")
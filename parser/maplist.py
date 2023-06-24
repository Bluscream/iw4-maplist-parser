from dataclasses import dataclass
from json import dumps, load

from .map import Map

@dataclass
class Maplist:
    game: str
    maps: dict[str,'Map']

    def get_maps_by_source(self):
        maps = {}
        for mapname, map in self.maps.items():
            if map.source.name not in maps:
                maps[map.source.name] = {}
            maps[map.source.name][mapname] = map
        return maps

    @staticmethod
    def from_dict(obj: dict) -> 'Maplist':
        maps = {}
        for game, _maps in obj.items():
            for mapname, map in _maps.items():
                maps[mapname] = Map.from_dict(map)
        sources = {map.source.name for map in maps.values()}
        print("Loaded", len(maps), "maps from", len(sources), "sources")
        return Maplist(game, maps)
    
    @staticmethod
    def load(file: str = 'maps.json'):
        with open(file, 'r') as f:
            jsonstring = load(f)
            return Maplist.from_dict(jsonstring)
    
    def save(self, file: str = 'maps.json'):
        json = dumps({self.game: self.maps}, default=lambda o: o.__dict__, sort_keys=True, indent=4) # , object_hook=remove_nulls
        if file:
            with open(file, 'w') as f: f.write(json)
        print("Saved ", len(self.maps), "maps to", file)
        return json
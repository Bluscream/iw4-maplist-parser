from parser.stringmap import StringMaps
from parser.maplist import Maplist, Map, Source

maplist = Maplist.load()

stringmaps = StringMaps()
stringmaps.parse_files(stringmaps.get_files())

for lang, strings in stringmaps.strings.items():
    print(lang, len(strings))

# with open('maps_main_dlc.txt', 'r') as f:
#     map_array = f.read().splitlines()
# source = Source("Base Game / DLC")
# for mapname in map_array:
#     maplist.maps[mapname] = Map.from_mapname(mapname, source, stringmaps)

# with open('maps_sp.txt', 'r') as f:
#     map_array = f.read().splitlines()
# source = Source("Single Player", "https://steamcommunity.com/groups/IW4X/discussions/0/1470841715980056455")
# for mapname in map_array:
#     maplist.maps[mapname] = Map.from_mapname(mapname, source, stringmaps)

# with open('maps_usermaps.txt', 'r') as f:
#     map_array = f.read().splitlines()
# source = Source("Custom Maps", "https://tinyurl.com/iw4xmaps")
# for mapname in map_array:
#     maplist.maps[mapname] = Map.from_mapname(mapname, source, stringmaps)

for mapname, map in maplist.maps.items():
    map.preview.update()
    map.minimap.update()

maplist.json('maps.out.json')

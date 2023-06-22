def splitList(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]
from itertools import islice
def splitDict(data, SIZE=15):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}
def pprint(msg): print(f"\t{msg}")

from parser.maplist import Maplist, Map, Source
maplist = Maplist.load()

maps = maplist.maps
maps_per_page = 15


map_pages = maplist.get_maps_by_source() # list(splitDict(maps, maps_per_page))
pages = len(map_pages)
for page_i, page in enumerate(map_pages):
    map: Map
    for i, mapname in enumerate(page):
        map = page[i]
        i-=1
        even = (i % 2) == 0
        name = f'{"^9" if even else ""}{map.name.get("english")}'
        pprint(f'MENU_MAP_BUTTON({page_i}, {i}, "{mapname}", "{mapname}", exec "rcon map {mapname}")')
        # print(f'MENU_CHOICE_BUTTON_VIS({i}, "button_{i+1}", "{name}", exec "rcon map {map}"; close self;, ;, 1)')
        # print(f'MENU_CHOICE_NEWICON_RAW({i}, "preview_{map}", 1)')
        # print(f'MENU_CHOICE_BUTTON_VIS({i}, ;, "{map}",setdvar ui_mapname {map};exec "rcon map {map}";close self;, 1, preview_{map}, {map}, {map})')
    
    if page_i+1 < pages:pprint(f'MENU_CHOICE_BUTTON_VIS({maps_per_page + 1}, ;, "Next", setLocalVarInt ui_page {page_i+1};, ;, when( localVarInt( ui_page ) == {page_i}))')
    if page_i+1 > 1:pprint(f'MENU_CHOICE_BUTTON_VIS({maps_per_page + 2}, ;, "Previous", setLocalVarInt ui_page {page_i-1};, ;, when( localVarInt( ui_page ) == {page_i}))')

print("")
pprint(f'MENU_CHOICE_BUTTON({maps_per_page + 3}, ;, "Back", close "self";, ;)')
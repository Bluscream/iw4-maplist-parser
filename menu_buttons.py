def splitList(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]
from itertools import islice, chain
def splitDict(data, SIZE=15):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}
def pprint(msg): print(f"\t{msg}")

from parser.maplist import Maplist, Map, Source
maplist = Maplist.load()

maps = maplist.maps
maps_per_page = 15


sources = maplist.get_maps_by_source() # list(splitDict(maps, maps_per_page))
sources_cnt = len(sources)
pi = 1
maps: dict[str, Map]
allpages = len(list(chain.from_iterable([list(splitDict(maps, maps_per_page)) for maps in sources.values()])))
for source, maps in sources.items():
    pprint(f"// SOURCE {source} WITH {len(maps)} MAPS\n")
    pages = list(splitDict(maps, maps_per_page))
    pages_cnt = len(pages)
    for page in pages:
        pprint(f"// PAGE {pi} OF {pages_cnt} WITH {len(page)} MAPS")
        # pprint(f'MENU_MAP_BUTTON({pi}, {0}, "{source}", "", "")')
        i = 1
        map: Map
        for mapname, map in page.items():
            # print("// MAP", mapname)
            even = (i % 2) == 0
            name = f'{"^9" if even else ""}{map.name.get("english")}'
            pprint(f'MENU_MAP_BUTTON({pi}, {i}, "{name}", "{map.description.get("english")}", exec "rcon map {mapname}")')
            # print(f'MENU_CHOICE_BUTTON_VIS({i}, "button_{i+1}", "{name}", exec "rcon map {map}"; close self;, ;, 1)')
            # print(f'MENU_CHOICE_NEWICON_RAW({i}, "preview_{map}", 1)')
            # print(f'MENU_CHOICE_BUTTON_VIS({i}, ;, "{map}",setdvar ui_mapname {map};exec "rcon map {map}";close self;, 1, preview_{map}, {map}, {map})')
            i+=1
        # print("pi", pi, "allpages", allpages)
        if pi < allpages:pprint(f'MENU_CHOICE_BUTTON_VIS({maps_per_page + 1}, ;, "Next", setLocalVarInt ui_page {pi+1};, ;, when( localVarInt( ui_page ) == {pi}))')
        if pi > 1:pprint(f'MENU_CHOICE_BUTTON_VIS({maps_per_page + 2}, ;, "Previous", setLocalVarInt ui_page {pi-1};, ;, when( localVarInt( ui_page ) == {pi}))')
        pi+=1

print("")
pprint(f'MENU_CHOICE_BUTTON({maps_per_page + 3}, ;, "Back", close "self";, ;)')
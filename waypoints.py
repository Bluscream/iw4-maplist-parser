from pathlib import Path
from sys import path as syspath
from os import getcwd
syspath.append(getcwd())
from waypoints.WaypointFile import WaypointFile, SortingMethod

ask_input = False
wp_dir = Path(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints")

# loop over csv files in S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints
for file in wp_dir.glob("*.csv"):
    file = WaypointFile(file, ask_for_user_input=ask_input)
    err = file.check(fix=True, ask_for_user_input=ask_input)
    file.save(file.path, sort=SortingMethod.NONE)

    

# file = WaypointFile(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_wp.csv", ask_for_user_input=ask_input)
# err = file.check(fix=True, ask_for_user_input=ask_input)
# file2 = WaypointFile(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_ext.csv", ask_for_user_input=ask_input, is_cut_file=True)
# err = file2.check(fix=True, ask_for_user_input=ask_input)
# # file2.waypoints = file2.waypoints[1:]
# # err = file2.check(fix=True, ask_for_user_input=ask_input)


# file.save(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_wp_fixed.csv", sort=SortingMethod.NONE)
# file.merge_from(file2)
# file.check(fix=True, ask_for_user_input=ask_input)
# for waypoint in file.waypoints:
#     print(waypoint)

# file2.save(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_wp_ext_fixed.csv", sort=SortingMethod.NONE)
# file.save(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_wp_merged.csv", sort=SortingMethod.NONE)
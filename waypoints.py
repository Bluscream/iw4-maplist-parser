from sys import path as syspath
from os import getcwd
syspath.append(getcwd())
from waypoints.WaypointFile import WaypointFile, SortingMethod

ask_input = True

file = WaypointFile(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_wp.csv", ask_for_user_input=ask_input)
err = file.check(fix=True, ask_for_user_input=ask_input)
file2 = WaypointFile(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_ext.csv", ask_for_user_input=ask_input, is_cut_file=True)
err = file2.check(fix=True, ask_for_user_input=ask_input)


file.merge_from(file2)
file.check(fix=True, ask_for_user_input=ask_input)
# for waypoint in file.waypoints:
#     print(waypoint)

file.save(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_wp_merged.csv", sort=SortingMethod.NONE)
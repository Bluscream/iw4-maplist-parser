from sys import path as syspath
from os import getcwd
syspath.append(getcwd())
from waypoints.WaypointFile import WaypointFile

ask_for_user_input = True

file = WaypointFile(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_wp.csv", ask_for_user_input=ask_for_user_input)
file.check(False)
input("Press enter to continue...")
file2 = WaypointFile(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_ext.csv", ask_for_user_input=ask_for_user_input, is_cut_file=True)
file2.check(False)
input("Press enter to continue...")


file.merge_from(file2)

# for waypoint in file.waypoints:
#     print(waypoint)

file.save(r"S:\Call of Duty\CoD 6 (MW2)\userraw\scriptdata\waypoints\co_hunted_wp_merged.csv", sort_by_distance=True)
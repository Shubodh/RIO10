import os
import argparse
from pathlib import Path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scene_type', type=str, required=True) # example: ROI_with_QOI
    parser.add_argument('--dttime', type=str, required=True) # dt030622-t1910
    parser.add_argument('--roomids', type=str, required=True) # 13579 
    parser.add_argument('--debug_print', choices=('True', 'False'), required=True)
    parser.add_argument('--augmented_query', choices=('True', 'False'), required=True)
    args = parser.parse_args()

    augmented_query_str = args.augmented_query
    scene_type = args.scene_type
    dttime = args.dttime #"dt030622-t1910"
    debug_print = args.debug_print == 'True'
    room_ids = list(args.roomids.strip(" ")) ##room_ids = ["1", "3", "5", "7", "9"]

    for room_id in room_ids:
        print("\n")
        print(room_id)
        print("python plot_scene0X.py --data_path ../data/ --type 2 --config ../config_graphVPR_sampling10_scene0" + room_id + ".json --scene_id 0" + room_id + " --scene_type " + scene_type + " --dttime " + dttime + " --augmented_query " + augmented_query_str)
        if not debug_print:
            os.system("python plot_scene0X.py --data_path ../data/ --type 2 --config ../config_graphVPR_sampling10_scene0" + room_id + ".json --scene_id 0" + room_id + " --scene_type " + scene_type + " --dttime " + dttime + " --augmented_query " + augmented_query_str)
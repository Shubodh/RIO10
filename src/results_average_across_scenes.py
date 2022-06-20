import os
import argparse
from pathlib import Path
import json
import numpy as np


if __name__ == '__main__':
    scene_types =["ROI_with_QOI" , "RRI_with_QRI" , "RRI_with_QOI" , "ROI_with_QRI"] # ["ROI_and_ARRI_with_QRI", "RRI_and_ARRI_with_QRI", "ROI_and_ARRI_with_QOI"]  #more: ROI_with_QOI, RRI_with_QRI,
    scene_types_aug_ref = ["ROI_and_ARRI_with_QRI", "RRI_and_ARRI_with_QRI","ROI_and_ARRI_with_QOI", "RRI_and_ARRI_with_QOI"]
    scene_types_aug_query = ["ROI_with_QOI_and_AQRI", "ROI_and_ARRI_with_QOI_and_AQRI", "RRI_with_QRI_and_AQRI", "RRI_and_ARRI_with_QRI_and_AQRI"]
    scene_types_aug_query_a = ["ROI_and_ARRI_with_QOI_and_AQRI", "RRI_and_ARRI_with_QRI_and_AQRI"]
    scene_types_aug_all = scene_types_aug_ref + scene_types_aug_query

    dttime = "dt100622-t0201"
    #dttime = "dt050622-t1111"
    #dttime = "dt030622-t1910"
    #room_ids = ["1"]
    room_ids = ["1", "3", "5", "7", "9"]

    scene_types_current = [scene_types_aug_ref[0], scene_types_aug_ref[1]]

    iter_i = 0
    print_individual = False
    for scene_type in scene_types_current:
        av_pose_200 = []
        av_pose_25 = []
        av_pose_5 = []
        if print_individual:
            print("\n")
            print("1. INDIVIDUAL RESULTS")
            print(f"  SCENE TYPE: {scene_type}")
        for room_id in room_ids:
            base_path = "/media/shubodh/DATA/OneDrive/rrc_projects/2021/graph-based-VPR/RIO10/data/results/" + scene_type + "/"
            file_prefix = "RIO_scene0" + room_id + "_hloc_d2net_NN_mutual_skip10"
            output_file_name = base_path + file_prefix + "_" +  "results_" + scene_type + "_scene0" + room_id + "_" + dttime  + ".json"
            assert Path(output_file_name).exists(), Path(output_file_name)
            with open(output_file_name, 'r') as openfile:
                json_object = json.load(openfile)
                iter_i += 1
                if print_individual:
                    print(scene_type, "room_id: ", room_id)
                    print('pose_200,   pose_25,   pose_5')
                    print(json_object['pose_200'], "   ", json_object['pose_25'], "   ", json_object['pose_5'])
                av_pose_200.append(json_object['pose_200'])
                av_pose_25.append(json_object['pose_25'])
                av_pose_5.append(json_object['pose_5'])
                # print(iter_i)
    
        print("\n")
        print("2. COMBINED AVERAGE RESULTS")
        print(f"  SCENE TYPE: {scene_type}")
        av_pose_200 = np.asarray(av_pose_200, dtype=float)
        av_pose_25 = np.asarray(av_pose_25, dtype=float)
        av_pose_5 = np.asarray(av_pose_5, dtype=float)
        print('pose_200, pose_25, pose_5 AVERAGED')
        print('{:.3}'.format(np.average(av_pose_200)), ",", '{:.3}'.format(np.average(av_pose_25)), ",", '{:.3}'.format(np.average(av_pose_5)))


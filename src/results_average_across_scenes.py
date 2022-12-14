import os
import argparse
from pathlib import Path
import json
import numpy as np


def main(method_type):
    # Date <> testing info
    #gt_radius_NETVLAD = "False" #dttime = "dt180622-t1511"
    #o20andr20 = "True" #dt200622-t1021
    scene_types =["ROI_with_QOI" , "RRI_with_QRI" , "RRI_with_QOI" , "ROI_with_QRI"] # ["ROI_and_ARRI_with_QRI", "RRI_and_ARRI_with_QRI", "ROI_and_ARRI_with_QOI"]  #more: ROI_with_QOI, RRI_with_QRI,
    scene_types_aug_ref = ["ROI_and_ARRI_with_QRI", "RRI_and_ARRI_with_QRI","ROI_and_ARRI_with_QOI", "RRI_and_ARRI_with_QOI"]
    scene_types_aug_query = ["ROI_with_QOI_and_AQRI", "ROI_and_ARRI_with_QOI_and_AQRI", "RRI_with_QRI_and_AQRI", "RRI_and_ARRI_with_QRI_and_AQRI"]
    scene_types_aug_query_a = ["ROI_and_ARRI_with_QOI_and_AQRI", "RRI_and_ARRI_with_QRI_and_AQRI"]
    scene_types_aug_all = scene_types_aug_ref + scene_types_aug_query

    # TODO: SET ALL THE BELOW, properly check.
    dttime = "dt141222-t1210"; type_test = "normal"
    # dttime = "dt081222-t0239"; type_test = "normal"
    # dttime = "dt061222-t2155"; type_test = "normal"
    # dttime = "dt230622-t2112"; type_test = "o40andgt40"
    # dttime = "dt100623-t2201"; type_test = "none_but_nvlad80"
    # dttime = "dt100622-t0201"; type_test = "normal"
    # dttime = "dt180622-t1511"; type_test = "gt_radius_NETVLAD"
    # dttime = "dt200622-t1021"; type_test = "o20andr20"
    # dttime = "dt210622-t1907"; type_test = "o40andr40"

    #dttime = "dt050622-t1111"
    #dttime = "dt030622-t1910"
    #room_ids = ["1"]
    room_ids = ["1", "3", "5", "7", "9"]
    # scene_types_current = [scene_types_aug_ref[0], scene_types_aug_ref[1]]
    # scene_types_current = [scene_types[0],  scene_types_aug_ref[2]]
    #scene_types_current = [scene_types_aug_ref[2],scene_types_aug_ref[3]]#, scene_types_aug_query[0],scene_types_aug_query[1],scene_types_aug_query[2], scene_types_aug_query[3]]
    # scene_types_current = [scene_types_aug_query[0],scene_types_aug_query[1],scene_types_aug_query[2], scene_types_aug_query[3]]
    # scene_types_current = [scene_types[0]]#,scene_types_aug_query[1],scene_types_aug_query[2], scene_types_aug_query[3]]
    scene_types_current = ["QRI_with_QOI"] # ["AQRI_with_QOI"]
    print_individual =  False
    # TODO: SET ALL THE ABOVE, properly check.


    iter_i = 0
    for scene_type in scene_types_current:
        av_pose_200 = []
        av_pose_25 = []
        av_pose_5 = []
        av_DCRE_5 = []
        av_DCRE_15 = []
        av_score = []

        if print_individual:
            print("\n")
            print("1. INDIVIDUAL RESULTS")
            print(f"  SCENE TYPE: {scene_type}")
        for room_id in room_ids:
            base_path = "/media/shubodh/DATA/OneDrive/rrc_projects/2021/graph-based-VPR/RIO10/data/results/" + scene_type + "/"
            # json_file_prefix = "RIO_scene0" + room_id + "_hloc_d2net_NN_mutual_skip10"
            
            if method_type == "MINE":
                json_file_prefix = "RIO_scene0" + room_id + "_hloc_d2net_NN_mutual_skip10"
            elif method_type == "d2net":
                json_file_prefix = "d2_net_sampling10_scene0" + room_id
            elif method_type == "grove_v2":
                json_file_prefix = "grove_v2_sampling10_scene0" + room_id
            else:
                raise ValueError("method_type not recognized")


            output_file_name = base_path + json_file_prefix + "_" +  "results_" + scene_type + "_scene0" + room_id + "_" + dttime  + ".json"
            assert Path(output_file_name).exists(), Path(output_file_name)
            with open(output_file_name, 'r') as openfile:
                json_object = json.load(openfile)
                iter_i += 1
                if print_individual:
                    print(scene_type, "room_id: ", room_id)
                    print('pose_200,   pose_25,   pose_5', 'DCRE_5', 'DCRE_15', 'score')
                    print(json_object['pose_200'], "   ", json_object['pose_25'], "   ", json_object['pose_5'], "   ", json_object['DCRE_5'], "   ", json_object['DCRE_15'], "   ", json_object['score'])
                av_pose_200.append(json_object['pose_200'])
                av_pose_25.append(json_object['pose_25'])
                av_pose_5.append(json_object['pose_5'])
                av_DCRE_5.append(json_object['DCRE_5'])
                av_DCRE_15.append(json_object['DCRE_15'])
                av_score.append(json_object['score'])
                # print(iter_i)
    
        print("\n")
        print("2. COMBINED AVERAGE RESULTS across scenes")
        print(f"  SCENE TYPE: {scene_type}")
        av_pose_200 = np.asarray(av_pose_200, dtype=float)
        av_pose_25 = np.asarray(av_pose_25, dtype=float)
        av_pose_5 = np.asarray(av_pose_5, dtype=float)
        av_DCRE_5 = np.asarray(av_DCRE_5, dtype=float)
        av_DCRE_15 = np.asarray(av_DCRE_15, dtype=float)
        av_score = np.asarray(av_score, dtype=float)
        print('pose_200, pose_25, pose_5, DCRE_5, DCRE_15, score AVERAGED')
        print('{:.3}'.format(np.average(av_pose_200)), ",", '{:.3}'.format(np.average(av_pose_25)), ",", '{:.3}'.format(np.average(av_pose_5)), ",", '{:.3}'.format(np.average(av_DCRE_5)), ",", '{:.3}'.format(np.average(av_DCRE_15)), ",", '{:.3}'.format(np.average(av_score)))
        print(dttime,type_test) 


if __name__ == '__main__':
    all_method_types = ["MINE", "d2net", "grove_v2"]

    for method_type in all_method_types:
        print(f"\n ### WHICH METHOD: {method_type} ###")
        main(method_type)


    # grove_v2_sampling10_scene09_results_AQRI_with_QOI_scene09_dt081222-t0239.json
    # RIO_scene01_hloc_d2net_NN_mutual_skip10_results_AQRI_with_QOI_scene01_dt081222-t0239.json
    # d2_net_sampling10_scene01_results_AQRI_with_QOI_scene01_dt081222-t0239.json

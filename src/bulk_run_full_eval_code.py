import os
import argparse


if __name__ == '__main__':
    scene_types =["ROI_with_QOI" , "RRI_with_QRI" , "RRI_with_QOI" , "ROI_with_QRI"] # ["ROI_and_ARRI_with_QRI", "RRI_and_ARRI_with_QRI", "ROI_and_ARRI_with_QOI"]  #more: ROI_with_QOI, RRI_with_QRI,
    scene_types_aug_ref = ["ROI_and_ARRI_with_QRI", "RRI_and_ARRI_with_QRI","ROI_and_ARRI_with_QOI", "RRI_and_ARRI_with_QOI"]
    scene_types_aug_query = ["ROI_with_QOI_and_AQRI", "ROI_and_ARRI_with_QOI_and_AQRI", "RRI_with_QRI_and_AQRI", "RRI_and_ARRI_with_QRI_and_AQRI"]
    scene_types_aug_query_a = ["ROI_and_ARRI_with_QOI_and_AQRI", "RRI_and_ARRI_with_QRI_and_AQRI"]
    scene_types_aug_all = scene_types_aug_ref + scene_types_aug_query



    parser = argparse.ArgumentParser()
    parser.add_argument('--debug_print', choices=('True', 'False'), required=True)
    args = parser.parse_args()

    debug_print = str(args.debug_print) # Set False if you actually want code to run

    # TODO: SET ALL THE BELOW, properly check.
    #dttime = "dt130622-t0402"
    dttime = "dt100622-t0201"
    #dttime = "dt050622-t1111"
    # dttime = "dt030622-t1910"

    roomids_str = "13579"
    #roomids_str = "1"
    # scene_types_current =  [scene_types[3]]
    scene_types_current = [scene_types_aug_ref[0], scene_types_aug_ref[1]]
    augmented_query = "False"
    
    # TODO: SET ALL THE ABOVE, properly check.

    for scene_type in scene_types_current:
        print("\n")
        print("\n")
        print("SCENE TYPE")
        print(scene_type)
        print("\n")
        print("\n")
        # 1. Renaming/copying pose prediction file:
        print("1. COPYING POSE PREDICTION FILE")
        copy_file_path = "/media/shubodh/DATA/OneDrive/rrc_projects/2021/graph-based-VPR/RIO10/data/predictions/bulk_copy_prediction_txt.py"
        print("python " + copy_file_path + " --scene_type " + scene_type + " --dttime " + dttime + " --roomids " + roomids_str + " --debug_print " + debug_print)
        os.system("python " + copy_file_path + " --scene_type " + scene_type + " --dttime " + dttime + " --roomids " + roomids_str + " --debug_print " + debug_print)

        # 2. Generate error file from prediction file using evaluate.py:
        print("\n")
        print("2. GENERATE ERROR FILE")
        evaluate_file_path = "/media/shubodh/DATA/OneDrive/rrc_projects/2021/graph-based-VPR/RIO10/evaluate.py"
        print("python " + evaluate_file_path+ " --augmented_query " + augmented_query + " --roomids " + roomids_str + " --debug_print " + debug_print)
        os.system("python " + evaluate_file_path+ " --augmented_query " + augmented_query + " --roomids " + roomids_str + " --debug_print " + debug_print)

        # 3. Generating results files
        print("\n")
        print("3. GENERATE RESULTS FILE")
        results_file_path = "bash_plot_scene0X.py"
        print("python " + results_file_path + " --scene_type " + scene_type + " --dttime " + dttime + " --roomids " + roomids_str + " --debug_print " + debug_print)
        os.system("python " + results_file_path + " --scene_type " + scene_type + " --dttime " + dttime + " --roomids " + roomids_str + " --debug_print " + debug_print)

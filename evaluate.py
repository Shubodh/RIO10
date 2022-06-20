import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--roomids', type=str, required=True) # 13579 
    parser.add_argument('--debug_print', choices=('True', 'False'), required=True)
    parser.add_argument('--augmented_query', choices=('True', 'False'), required=True)
    args = parser.parse_args()

    room_ids = list(args.roomids.strip(" ")) ##room_ids = ["1", "3", "5", "7", "9"]
    debug_print = args.debug_print == 'True'
    augmented_query = args.augmented_query == 'True'
    # room_ids = ["1", "3", "5", "7", "9"]
    # # sp_or_d2net = "superpoint_inloc+superglue" #"d2net-ss+NN-mutual"

    for room_id in room_ids:
        print("\n")
        print(room_id)

        ### 1.a RIO_d2net
        base_path = "/media/shubodh/DATA/OneDrive/rrc_projects/2021/graph-based-VPR/RIO10/"
        if not augmented_query:
            print(base_path + "src/eval/build/eval_sampling10_scene0"+room_id+" " +base_path+"data/ " +base_path+"data/predictions/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt " +base_path+"data/errors/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt")
            if not debug_print:
                os.system(base_path + "src/eval/build/eval_sampling10_scene0"+room_id+" " +base_path+"data/ " +base_path+"data/predictions/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt " +base_path+"data/errors/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt")
        else:
            print(base_path + "src/eval/build/eval_sampling10_scene0"+room_id+"_queryAND"+" " +base_path+"data/ " +base_path+"data/predictions/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt " +base_path+"data/errors/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt")
            if not debug_print:
                os.system(base_path + "src/eval/build/eval_sampling10_scene0"+room_id+"_queryAND"+" " +base_path+"data/ " +base_path+"data/predictions/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt " +base_path+"data/errors/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt")

        ### 1.b RIO_d2net queryAND
        # print("./src/eval/build/eval_sampling10_scene0"+room_id+ "_queryAND" + " data/ data/predictions/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt data/errors/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt")
        # os.system("./src/eval/build/eval_sampling10_scene0"+room_id+ "_queryAND"+ " data/ data/predictions/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt data/errors/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt")

        ### 2. given grove_v2
        
        # print("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/grove_v2_sampling10_scene0"+room_id+".txt data/errors/grove_v2_sampling10_scene0"+room_id+".txt")
        # os.system("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/grove_v2_sampling10_scene0"+room_id+".txt data/errors/grove_v2_sampling10_scene0"+room_id+".txt")

        ## 3. given d2net 
        # print("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/d2_net_sampling10_scene0"+room_id+".txt data/errors/d2_net_sampling10_scene0"+room_id+".txt")
        # os.system("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/d2_net_sampling10_scene0"+room_id+".txt data/errors/d2_net_sampling10_scene0"+room_id+".txt")
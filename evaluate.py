import os


if __name__ == '__main__':
    room_ids = ["1", "3", "5", "7", "9"]
    for room_id in room_ids:
        print("\n")
        print(room_id)

        ### 1. RIO_d2net
        print("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt data/errors/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt")
        os.system("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt data/errors/RIO_scene0"+room_id+"_hloc_d2net_NN_mutual_skip10.txt")


        ### 2. given grove_v2
        
        # print("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/grove_v2_sampling10_scene0"+room_id+".txt data/errors/grove_v2_sampling10_scene0"+room_id+".txt")
        # os.system("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/grove_v2_sampling10_scene0"+room_id+".txt data/errors/grove_v2_sampling10_scene0"+room_id+".txt")

        ## 3. given d2net 
        # print("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/d2_net_sampling10_scene0"+room_id+".txt data/errors/d2_net_sampling10_scene0"+room_id+".txt")
        # os.system("./src/eval/build/eval_sampling10_scene0"+room_id+" data/ data/predictions/d2_net_sampling10_scene0"+room_id+".txt data/errors/d2_net_sampling10_scene0"+room_id+".txt")
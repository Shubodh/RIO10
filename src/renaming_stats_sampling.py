from pathlib import Path
import sys
import logging
import argparse

def parse_poses_from_file(pose_path, sampling_rate):
    poses = []
    with open(pose_path, 'r') as f:
        for line in f:
            line = line.strip('\n')
            name, *data = line.split()
            if len(line) == 0 or line[0] == '#' or name == 'frame':
                continue
            poses.append((name, data))


    assert len(poses) > 0
    print(f'Imported {len(poses)} poses from {pose_path}')
    return poses

def write_results_to_file(path, img_poses_list, sampling_rate):
    # img_poses_list: [(img_name_1, pose_1), (_2, _2)..]. pose_1 is [qw, qx, qy, qz]
#            poses_outpath = (pose_path.parents[0]) /  Path(str(pose_path.stem) + "_sampling" + str(sampling_rate) + ".txt")
#            with open(poses_outpath, 'w') as fw:
#
#                end_int = int(''.join(filter(str.isdigit, name)))
#
#                if end_int % sampling_rate == 0:
#                    print(name,"hi", data, end_int, sampling_rate)
#                    sys.exit()
#                    fw.append(f'{name} {data}\n')

    with open(path, 'w') as f:
        for name, pose in img_poses_list:
            end_int = int(''.join(filter(str.isdigit, name)))
            if end_int % 10 == 0:
                qvec, tvec = pose[:4], pose[4:]
                qvec = ' '.join(map(str, qvec))
                tvec = ' '.join(map(str, tvec))
                # name = q.split("/")[-1]
                f.write(f'{name} {qvec} {tvec}\n')
    print(f'Written {len(img_poses_list)} poses to {path.name}')

if __name__ == "__main__":
    # main_dummy()
    parser = argparse.ArgumentParser()
    parser.add_argument('--pose_path', type=Path, required=True)
    args = parser.parse_args()
    sampling_rate = 10
    poses = parse_poses_from_file(args.pose_path, sampling_rate)

    pose_outpath = (args.pose_path.parents[0]) /  Path(str(Path(args.pose_path).stem) + "_sampling" + str(sampling_rate) + ".txt")
    write_results_to_file(pose_outpath, poses, sampling_rate)

    # main_check_read_write_depth()
    # pose_path = Path("outputs/rio/full/RIO_hloc_d2net-ss+NN-mutual_skip10_dt160222-t0411.txt")
    # convert_pose_file_format_wtoc_to_ctow(pose_path)

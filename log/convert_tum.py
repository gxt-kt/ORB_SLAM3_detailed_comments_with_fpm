# 功能： 将位姿txt文件中的第一列时间戳由纳秒单位转成秒单位
import numpy as np
import os, sys
 
file_path = "./tum_room1_512_mono_imu_g2o.txt"
new_path = "./new_tum_room1_512_mono_imu_g2o.txt"

def main():
    file = open(file_path, "r")
    lines = file.readlines()
    new_line = ""
    for line in lines:
        val = float(line.split(' ')[0])
        val = val / 1e9
        val_str = str(val)
        new_line = line
        new_line = new_line.replace(new_line.split(' ')[0], val_str)
        with open(new_path, 'a') as f:
            f.writelines(new_line)
 
if __name__ == "__main__":
    main()
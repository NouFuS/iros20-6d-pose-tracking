# -*- coding: UTF-8 -*-
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

import os, sys, glob, shutil
from pprint import pprint

path = "/home/qb26/scratch60/generated_data/"
# path = "/home/qb26/scratch60/_badScale_generated_data/"

all_folders = os.listdir(path)
all_master_names = {}
total_data_points = 0
pprint(all_folders)

map_to_aggregate = []
idx = 1
for folder in all_folders:
    file_masters = set()
    for name in os.listdir(os.path.join(path, folder)):
        file_masters.add(name[0:7])

    for master_name in file_masters:
        map_to_aggregate.append((format(idx, '07d'), os.path.join(path, folder, master_name)))    
        idx+=1
    all_master_names.update({int(folder):file_masters})
    total_data_points += len(file_masters)

print("Total nb of datapoints:", total_data_points)

print("*"*10, "Starting Copying")
target_folder = "/home/qb26/scratch60/aggregated_data_goodK/"
if not os.path.exists(target_folder):
    os.mkdir(target_folder)

tracking_idx = 1
for new_path, old_path in map_to_aggregate:
    # print("\nMapping:", old_path, "to", new_path)
    for to_copy in glob.glob(old_path+"*"):
        old_index = old_path.split("/")[-1]
        updated_path = os.path.join(target_folder, to_copy.replace(old_index, new_path).split("/")[-1])
        shutil.copy(to_copy, updated_path)
    tracking_idx +=1
    if tracking_idx % 10 == 0:
        printProgressBar(tracking_idx, total_data_points)

print("DONE")
#!/bin/bash

#SBATCH --job-name=dataset_aggregation_cpu
#SBATCH --output=dataset_aggregation_job_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --partition=day
#SBATCH --time=1-00:00:00


cd /home/qb26/Documents/se3-tracking/iros20-6d-pose-tracking
python3 aggregate_data.py
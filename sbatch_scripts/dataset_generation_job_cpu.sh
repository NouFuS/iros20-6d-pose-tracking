#!/bin/bash

#SBATCH --job-name=dataset_generation_cpu
#SBATCH --output=dataset_generation_job_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --partition=day
#SBATCH --time=1-00:00:00


cd /home/qb26/Documents/iros20-6d-pose-tracking
singularity exec se3_tracker.sif python blender_main.py -1
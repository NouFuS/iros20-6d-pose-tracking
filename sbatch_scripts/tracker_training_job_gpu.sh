#!/bin/bash

#SBATCH --job-name=tracker_training
#SBATCH --output=tracker_training_job_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=36
#SBATCH --gpus=1
#SBATCH --partition=gpu
#SBATCH --time=1-00:00:00

cd /home/qb26/Documents/iros20-6d-pose-tracking
module load miniconda
conda activate train_env
python train.py
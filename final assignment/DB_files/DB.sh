#!/bin/bash

#SBATCH --job-name="DB_runn"
#SBATCH --time=06:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=40
#SBATCH --partition=compute
#SBATCH --mem-per-cpu=4GB
#SBATCH --account=Education-TPM-MSc-EPA

#SBATCH --mail-type=ALL
#SBATCH --mail-user=r.kooijman-1@student.tudelft.nl


module load 2023r1
module load openmpi
module load python
module load py-numpy
module load py-scipy
module load py-mpi4py
module load py-pip

echo "Starting my job..."
pip install --user --upgrade ema_workbench
pip install --user networkx
pip install --user openpyxl
pip install --user xlrd
pip install --user ipyparallel

mpiexec -n 1 python dike_model_multi_scenario_MORDM.py




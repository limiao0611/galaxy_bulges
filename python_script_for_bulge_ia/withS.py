#!/bin/bash
#SBATCH -N1 --ntasks-per-node=40 --exclusive -o OUTPUT  -p bnlx
#SBATCH --mail-user=mli@flatironinstitute.org
#SBATCH --mail-type=BEGIN,END,FAIL
source ~/.bash_profile
module load gcc
module load openmpi
export LD_LIBRARY_PATH=$YT_DEST/lib:$LD_LIBRARY_PATH
#mpirun ./enzo.exe GalaxyDiskPatch.enzo
mpirun ./enzo.exe -r DD0161/sb_0161 >> OUTPUT_from_161

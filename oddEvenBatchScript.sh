#!/bin/bash 
#SBATCH --partition=standard
#SBATCH --qos=normal
#SBATCH --job-name=myJobName  #optional name to give to your job 
#SBATCH -c 1 # Number of CPUS requested. If omitted, the default is 1 CPU. 
#SBATCH --mem=4G # Memory requested in megabytes. If omitted, the default is 1024 MB. 
#SBATCH --time=00:30:00 # Expected job run time (killed afterwards) default 3hrs. 

python oddEvenSync.py


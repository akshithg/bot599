#!/bin/bash
#$ -S /bin/bash
#$ -V
#$ -N Gee
#$ -cwd
#$ -o gee.log
#$ -j y
#$ -t 1-10:1

###

export PATH="/usr/local/cuda/bin:/local/cluster/miniconda2/bin:$PATH"
export LD_LIBRARY_PATH="/local/cluster/cuda/lib64"

python ../feature_calculator.py <inputdir> $SGE_TASK_ID <outputdir>

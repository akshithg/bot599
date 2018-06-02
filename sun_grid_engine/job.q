#!/bin/bash
#$ -S /bin/bash
#$ -V
#$ -N Gee
#$ -cwd
#$ -o gee.log
#$ -j y
#$ -t 1-5:1

input=$1
output=$2

export PATH="/usr/local/cuda/bin:/local/cluster/miniconda2/bin:$PATH"
export LD_LIBRARY_PATH="/local/cluster/cuda/lib64"

python feature_calculator.py $input$SGE_TASK_ID $output$SGE_TASK_ID

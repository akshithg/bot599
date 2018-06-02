#!/bin/bash
#$ -S /bin/bash
#$ -V
#$ -N Gee
#$ -cwd
#$ -o gee_m.log
#$ -j y
#$ -l mem_free=2.0G
#$ -t 1-5:1

python ../feature_calculator.py <inputdir> $SGE_TASK_ID <outputdir>

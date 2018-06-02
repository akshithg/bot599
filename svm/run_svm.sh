#!/bin/bash

# usage ./run_svm.sh <file_a> <file_b>

export R_LIBS=$R_LIBS:/local/cluster/R_Packages/3.3

class_a=$1
class_b=$2

Rscript quick_svm.R $class_a $class_b

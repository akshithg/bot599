'''
file join
usage: python merge_features.py directory output_file
'''

import sys
import os

def usage_str():
    '''
    usage string
    '''
    print("usage: python merge_features.py <directory> <output_file>")

def decorator(n):
    '''
    '''
    print("*"*n)

def join_files(directory, output_file):
    '''
    join all input_files into one output_file
    '''
    # Files in directory
    print("files in the directory:")
    input_files = []
    for file in os.listdir(directory):
        file = directory + "/" + file
        print(file)
        input_files.append(file)

    print("\nwriting to :"+output_file)
    output_file = open(output_file, "w")

    write_header = False
    for file in input_files:
        file = open(file)
        header = file.readline()
        data = file.readlines()

        # write header once
        if not write_header:
            output_file.write(header)
            write_header = True

        for line in data:
            output_file.write(line)

        file.close()

    # close output file
    output_file.flush()
    output_file.close()


# **** Starts here ****
decorator(25)

# read file and p from args
if(len(sys.argv) < 3):
    usage_str()
else:
    join_files(sys.argv[1], sys.argv[2])
    print("DONE")

decorator(25)

'''
file chop chop
usage: python file_splitter.py <file> <splits>
'''

import sys
import os

def usage_str():
    '''
    usage string
    '''
    print("usage: python file_splitter.py <file> <splits>")

def decorator(n):
    '''
    '''
    print("*"*n)

def split_file(path, splits):
    '''
    splits file
    '''
    input_file = open(path)
    # read header line
    header = input_file.readline()
    # read rest of the data
    data = input_file.readlines()
    # total lines
    total_lines = len(data)
    # calculate line per chop
    lines_per_split = int(total_lines / splits) + (total_lines % splits > 0)

    # create output dir
    output_path = path + ".splits"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # write into each split
    print("Part files:")
    for i in range(splits):
        # create a part file
        part_file = output_path+"/part"+str(i+1)
        print(part_file)
        part_file = open(part_file, "w")

        # write header
        part_file.write(header)

        # write data
        for line in data[i*lines_per_split : i*lines_per_split + lines_per_split]:
            part_file.write(line)

        # close file
        part_file.flush()
        part_file.close()




# **** Starts here ****
decorator(25)

# read file and p from args
if(len(sys.argv) < 2):
    usage_str()
else:
    try:
        chops = int(sys.argv[2])
    except:
        usage_str()
    else:
        split_file(sys.argv[1], chops)

    print("DONE")

decorator(25)

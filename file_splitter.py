'''
file chop chop
usage: python file_splitter.py file NUMBER_OF_CHOPS
'''

import sys

def usage_str():
    '''
    usage string
    '''
    print("usage: python file_splitter.py file number_of_parts")

def decorator(n):
    '''
     ¯\_(ツ)_/¯
    '''
    print("*"*n)

def split_file(path, chops):
    '''
    splits file into n chops
    '''
    file = open(path)

    # read header line
    header = file.readline()
    # read resst of the data
    data = file.readlines()

    # total lines
    total_lines = len(data)
    # calculate line per chop
    lines_per_chop = int(total_lines / chops) + (total_lines % chops > 0)
    print("Part files:")
    for i in range(chops):
        # create a part file
        part_file = path+".part"+str(i+1)
        print(part_file)
        part_file = open(part_file, "w")

        # write header
        part_file.write(header)

        # write data
        for line in data[i*lines_per_chop : i*lines_per_chop + lines_per_chop]:
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

decorator(25)
print("DONE")

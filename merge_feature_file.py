'''
file join
usage: python file_splitter.py file1 file2 [file3] ... [fileN] outputfile
'''

import sys

def usage_str():
    '''
    usage string
    '''
    print("usage: python file_splitter.py file1 file2 [file3] ... [fileN] outputfile")

def decorator(n):
    '''
    '''
    print("*"*n)

def join_files(input_files, output_file):
    '''
    join all input_files into one output_file
    '''
    print("writing to :"+output_file)
    output_file = open(output_file, "w")

    write_header = False
    for file in input_files:
        print("reading from: "+file)
        file = open(file)
        header = file.readline()
        data = file.readlines()

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
    join_files(sys.argv[1:-1], sys.argv[-1])

decorator(25)
print("DONE")

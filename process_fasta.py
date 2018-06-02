'''
clean and format fasta files
default output: <input_file_path>.clean
usage: python pocess_fasta.py <fasta_file> [output_file]
'''

import sys

COLUMNS = ['gene_stable_id', 'transcript_stable_id', 'seq']

def usage_str():
    '''
    usage string
    '''
    print("usage: python pocess_fasta.py <fasta_file> [output_file]")

def decorator(n):
    '''
    '''
    print("*"*n)

def header_line():
    '''
    returns the header line
    '''
    return ",".join(COLUMNS)

def format_data_line(line):
    '''
    formats each line into comma separated values
    '''
    data_line = line[:15] + "," + line[15:30] + "," + line[30:]
    return data_line

def fasta_format(path, output_file):
    '''
    cleans and formats file and writes to file.clean
    removes Sequence unavailable lines too
    '''
    print("formatting file: "+path)
    # create a file handler
    input_file = open(path, 'r')

    # read, replace new line, split at >
    lines = input_file.read()\
                      .replace("\n", "")\
                      .replace("|", "")\
                      .split(">")[1:]

    # close file
    input_file.close()

    # write to output file
    print("writing to: "+output_file)
    output_file = open(output_file, "w")

    # write header line
    output_file.write(header_line()+"\n")
    # write data lines
    for line in lines:
        if(not "Sequence unavailable" in line):
            output_file.write(format_data_line(line) + "\n")

    # flush and close file.clean
    output_file.flush()
    output_file.close()


# **** Starts here ****
decorator(25)
# read file from args
if(len(sys.argv) < 2):
    usage_str()
else:
    try:
        fasta_format(path=sys.argv[1], output_file=sys.argv[2])
    except:
        fasta_format(path=sys.argv[1], output_file=sys.argv[1]+".clean")

    print("DONE")

decorator(25)

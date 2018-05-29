'''
clean and format fasta files
'''

import sys

COLUMNS = ['gene_stable_id', 'transcript_stable_id', 'seq']

def decorator(n):
    print("*"*n)

def header_line():
    return ",".join(COLUMNS)

def format_data_line(line):
    data_line = line[:15] + "," + line[15:30] + "," + line[30:]
    return data_line

def fasta_format(path):
    # create a file handler
    file = open(path, 'r')

    # read, replace new line, split at >
    lines = file.read()\
                .replace("\n", "")\
                .replace("|", "")\
                .split(">")[1:]

    # close file
    file.close()

    # write to a new file
    new_file = open(path+".clean", "w")

    # write header line
    new_file.write(header_line()+"\n")
    # write data lines
    for line in lines:
        if(not "Sequence unavailable" in line):
            new_file.write(format_data_line(line) + "\n")

    # flush and close file.clean
    new_file.flush()
    new_file.close()

# Starts here
decorator(25)
# read file from args
if(len(sys.argv) < 2):
    print("usage: python pocess_fasta.py file1 [file2] ... [fileN]")
else:
    for file in (sys.argv[1:]):
        # formats file
        print("formatting file: "+file)
        fasta_format(file)

decorator(25)
print("DONE")

'''
calculates features for a given file
usage: python feature_calculator.py <file_with_clean_data> [output_file]
'''
# for python 2 backward compatibility
from __future__ import division

import sys
import os
import pandas as pd
import re
import code


def usage_str():
    '''
    usage string
    '''
    print("usage: python feature_calculator.py <file_with_clean_data> [output_file]")

def decorator(n):
    '''
    '''
    print("*"*n)

class FeatureCalculator:
    def __init__(self, source_file):
        self.source_file = source_file
        self.data = pd.read_csv(source_file, skip_blank_lines=True)
        self.set_sequence_column()
        self.data.index.name = 'seq_no'
        self.non_feature_columns = self.data.columns.tolist()

    def set_sequence_column(self, seq="seq"):
        self.SEQ = seq

    def feature_columns(self):
        return list(set(self.data.columns.tolist()) - set(self.non_feature_columns))

    def save_features(self, columns=[], output_file=""):
        '''
        exports all data with features to a new file
        '''
        if not columns:
            columns = self.data.columns.tolist()

        if output_file == "":
            output_file = self.source_file + ".feature"

        self.data.to_csv(output_file, sep='\t', columns=columns)
        print("saving features: "+str(columns))
        print("Saved to " + output_file)


    def gc_content(self):
        '''
        feature: adds gc_content attribute
        '''
        print ("calculating GC content")

        def calc(seq):
            g = seq.count('G')
            c = seq.count('C')
            return ( (g+c) / len(seq) ) * 100

        self.data['gc_content'] = self.data[self.SEQ].apply(calc)
        return self.data


    def tataaa_box_present(self):
        '''
        feature: adds tataaa box attribute
        '''
        print ("calculating TATAAA box")

        def calc(seq):
            return int('TATAA' in seq)

        self.data['tataaa'] = self.data[self.SEQ].apply(calc)
        return self.data


    def gc_box(self):
        '''
        feature: adds gc box attribute: CCAAT and GGGCGG
        '''
        print ("calculating GC box")

        def calc(seq):
            gc = ['CCAAT', 'GGGCGG']
            return int(any(s in gc for s in seq))

        self.data['gc_box'] = self.data[self.SEQ].apply(calc)
        return self.data


    def poly_a_tail(self, n=3):
        '''
        3 or more As in last 36 nucleotide
        '''
        print ("calculating poly A tail")

        def calc(seq):
            if len(seq) < 36:
                return 0

            seq = seq[-36:]
            pattern = 'A{'+str(n)+'"'
            matches = re.findall(pattern, seq)

            return len(matches)

        self.data['poly_a'] = self.data[self.SEQ].apply(calc)
        return self.data


    def stop_codon_present(self):
        '''
        Checks for stop codons TAA TGA TAG
        '''
        print ("calculating stop codons")

        def calc(seq):
            STOP = ["TAA", "TGA", "TAG"]
            # check in any of the stop codons are in the seq
            return int(any(sc in STOP for sc in seq))

        self.data['stop_codon_present'] = self.data[self.SEQ].apply(calc)
        return self.data


    def sequence_length(self):
        '''
        calculates length of the seq
        '''
        print("calcualting sequence length")

        def calc(seq):
            return len(seq)

        self.data['seq_length'] = self.data[self.SEQ].apply(calc)
        return self.data


    def start_codon(self):
        '''
        Checks for start codons TAC
        '''
        print("checking for start codon")
        def calc(seq):
            return int("TAC" in seq)

        self.data['start_codon'] = self.data[self.SEQ].apply(calc)
        return self.data


    def feature_template(self):
        '''
        feature: adds new attribute
        '''
        print("calculating ... ? ")
        def calc(seq):
            # CHANGE THIS
            # val = calculate feature value on seq
            val = 0
            return val

        self.data['CHANGE_THIS_to_your_feature_name'] = self.data[self.SEQ].apply(calc)
        return self.data


## starts here
decorator(25)

if(len(sys.argv) < 2):
    usage_str()
else:
    feature_calculator = FeatureCalculator(sys.argv[1])

    # # interactive run
    # decorator(25)
    # print("`feature_calculator` object created, you can now interact with it")
    # decorator(25)
    # code.interact(local=dict(globals(), **locals()))


    # calculate features
    feature_calculator.gc_content()
    feature_calculator.tataaa_box_present()
    feature_calculator.gc_box()
    feature_calculator.poly_a_tail()
    feature_calculator.stop_codon_present()
    feature_calculator.start_codon()
    feature_calculator.sequence_length()

    # save features to file
    if(len(sys.argv)==3):
        output_file = sys.argv[2]
    else:
        output_file = ""

    feature_calculator.save_features(feature_calculator.feature_columns(), output_file)

    print("DONE")

decorator(25)

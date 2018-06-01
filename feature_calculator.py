'''
calculates features for a given file
'''

import sys
import pandas as pd
import re
import code


def usage_str():
    '''
    usage string
    '''
    print("python feature_calculator.py file_with_clean_data")

def decorator(n):
    '''
    '''
    print("*"*n)

class FeatureCalculator:
    def __init__(self, source_file):
        self.source_file = source_file
        self.data = pd.read_csv(source_file, skip_blank_lines=True)
        self.data.index.name = 'seq_no'
        self.SEQ = 'seq'


    def set_sequence_column(self, seq):
        self.SEQ = seq


    def save_features(self, columns=[]):
        '''
        exports all data with features to a new file
        '''
        if not columns:
            columns = self.data.columns.tolist()

        feature_file = self.source_file+"._features"
        self.data.to_csv(feature_file, sep=',', columns=columns)
        print("Saved to " + feature_file)


    def gc_content(self):
        '''
        feature: adds gc_content attribute
        '''
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
        def calc(seq):
            return int('TATAA' in seq)

        self.data['tataaa'] = self.data[self.SEQ].apply(calc)
        return self.data


    def gc_box(self):
        '''
        feature: adds gc box attribute: CCAAT and GGGCGG
        '''
        def calc(seq):
            gc = ['CCAAT', 'GGGCGG']
            return int(any(s in gc for s in seq))

        self.data['gc_box'] = self.data[self.SEQ].apply(calc)
        return self.data


    def poly_a_tail(self, n=3):
        '''
        3 or more As in last 36 nucleotide
        '''
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
        Checks of  on stop codons TAA TGA TAG
        '''
        def calc(seq):
            STOP = ["TAA", "TGA", "TAG"]
            # check in any of the stop codons are in the seq
            return int(any(sc in STOP for sc in seq))

        self.data['stop_codon_present'] = self.data[self.SEQ].apply(calc)
        return self.data


    def feature_template(self):
        '''
        feature: adds new attribute
        '''
        def calc(seq):
            # CHANGE THIS
            # val = calculate feature value on seq
            return val

        self.data['CHANGE_THIS_to_your_feature_name'] = self.data[self.SEQ].apply(calc)
        return self.data


## starts here

if(len(sys.argv) != 2):
    usage_str()
else:
    feature_calculator = FeatureCalculator(sys.argv[1])
    decorator(25)
    print("`feature_calculator` object created, you can now interact with it")
    decorator(25)
    code.interact(local=dict(globals(), **locals()))

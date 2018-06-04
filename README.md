# BOT599

## Clone this repo

<pre>
git clone https://github.com/akshithg/bot599.git && cd bot599
</pre>

### 1. Get those FASTA File

Files:
<pre>
.
├── README.md
├── data
│   ├── <b>3prime.fasta</b>
│   ├── <b>5prime.fasta</b>
│   └── <b>human_exon.fasta</b>
├── feature_calculator.py
├── file_splitter.py
├── merge_feature_file.py
└── process_fasta.py
</pre>

### 2. Clean'em up

Usage: `python process_fasta.py <fasta_file>`

Example:
<pre>
python process_fasta.py ./data/3prime.fasta
python process_fasta.py ./data/5prime.fasta
</pre>

<pre>
.
├── README.md
├── data
│   ├── 3prime.fasta
│   ├── <b>3prime.fasta.clean</b>
│   ├── 5prime.fasta
│   ├── <b>5prime.fasta.clean</b>
│   └── human_exon.fasta
├── feature_calculator.py
├── file_splitter.py
├── merge_feature_file.py
└── process_fasta.py
</pre>

### 3. Files are too big apparantly, split'em

Usage: `python file_splitter.py <clean_fasta_file> <pieces>`

Example:
<pre>
python file_splitter.py data/3prime.fasta.clean 5
python file_splitter.py data/5prime.fasta.clean 5
</pre>

Files:
<pre>
.
├── README.md
├── data
│   ├── 3prime.fasta
│   ├── 3prime.fasta.clean
│   ├── 3prime.fasta.clean.splits
│   │   ├── <b>part1</b>
│   │   ├── <b>part2</b>
│   │   ├── <b>part3</b>
│   │   ├── <b>part4</b>
│   │   └── <b>part5</b>
│   ├── 5prime.fasta
│   ├── 5prime.fasta.clean
│   ├── 5prime.fasta.clean.splits
│   │   ├── <b>part1</b>
│   │   ├── <b>part2</b>
│   │   ├── <b>part3</b>
│   │   ├── <b>part4</b>
│   │   └── <b>part5</b>
│   └── human_exon.fasta
├── feature_calculator.py
├── file_splitter.py
├── merge_feature_file.py
└── process_fasta.py
</pre>

### 4. Calculate those magic numbers

All the features are defined in `feature_calculator.py`, if you don't need something, comment it.

<pre>
...

# features
feature_calculator.gc_content()
feature_calculator.tataaa_box_present()
feature_calculator.gc_box()
feature_calculator.poly_a_tail()
feature_calculator.stop_codon_present()
feature_calculator.sequence_length()

# save features to file
feature_calculator.save_features(feature_calculator.feature_columns())

...
</pre>

#### A. To run on a single file without the Sun Grid Engine

Usage: `python feature_calculator.py <clean_fasta_file> [output_file]`

#### B. To process with the Sun Grid Engine

Usage: `qsub ./sun_grid_engine/job.q <input> <output>`

Example:
<pre>
mkdir data/class1
mkdir data/class2
qsub ./sun_grid_engine/job.q data/5prime.fasta.clean.splits/part data/class1/feature
qsub ./sun_grid_engine/job.q data/3prime.fasta.clean.splits/part data/class2/feature
</pre>

<pre>
.
├── README.md
├── data
│   ├── 3prime.fasta
│   ├── 3prime.fasta.clean
│   ├── 3prime.fasta.clean.splits
│   │   ├── part1
│   │   ├── part2
│   │   ├── part3
│   │   ├── part4
│   │   └── part5
│   ├── 5prime.fasta
│   ├── 5prime.fasta.clean
│   ├── 5prime.fasta.clean.splits
│   │   ├── part1
│   │   ├── part2
│   │   ├── part3
│   │   ├── part4
│   │   └── part5
│   ├── class1
│   │   ├── <b>feature1</b>
│   │   ├── <b>feature2</b>
│   │   ├── <b>feature3</b>
│   │   ├── <b>feature4</b>
│   │   └── <b>feature5</b>
│   ├── class2
│   │   ├── <b>feature1</b>
│   │   ├── <b>feature2</b>
│   │   ├── <b>feature3</b>
│   │   ├── <b>feature4</b>
│   │   └── <b>feature5</b>
│   └── human_exon.fasta
├── feature_calculator.py
├── file_splitter.py
├── merge_feature_file.py
└── process_fasta.py
</pre>

### 5. One Big File

Usage: `python merge_features.py <directory> <output_file>`

Example:
<pre>
python merge_feature_file.py data/class1 data/class1_features
python merge_feature_file.py data/class2 data/class2_features
</pre>

<pre>
.
├── README.md
├── data
│   ├── 3prime.fasta
│   ├── 3prime.fasta.clean
│   ├── 3prime.fasta.clean.splits
│   │   ├── part1
│   │   ├── part2
│   │   ├── part3
│   │   ├── part4
│   │   └── part5
│   ├── 5prime.fasta
│   ├── 5prime.fasta.clean
│   ├── 5prime.fasta.clean.splits
│   │   ├── part1
│   │   ├── part2
│   │   ├── part3
│   │   ├── part4
│   │   └── part5
│   ├── class1
│   │   ├── feature1
│   │   ├── feature2
│   │   ├── feature3
│   │   ├── feature4
│   │   └── feature5
│   ├── <b>class1_features</b>
│   ├── class2
│   │   ├── feature1
│   │   ├── feature2
│   │   ├── feature3
│   │   ├── feature4
│   │   └── feature5
│   ├── <b>class2_features</b>
│   └── human_exon.fasta
├── feature_calculator.py
├── file_splitter.py
├── merge_feature_file.py
└── process_fasta.py
</pre>

### 6. Run'em through SVM

<pre>
cd svm
./run_svm.sh ../data/class1_features ../data/class2_features
</pre>

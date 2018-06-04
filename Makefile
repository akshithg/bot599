all:
	echo "1. make features, once sge jobs complete 2. make svm"

features: clean process_fasta split build_features

svm: merge_files run_svm

process_fasta:
	python process_fasta.py ./data/3prime.fasta
	python process_fasta.py ./data/5prime.fasta

split:
	python file_splitter.py data/3prime.fasta.clean 5
	python file_splitter.py data/5prime.fasta.clean 5

build_features:
	mkdir data/class1
	mkdir data/class2
	qsub ./sun_grid_engine/job.q data/5prime.fasta.clean.splits/part data/class1/feature
	qsub ./sun_grid_engine/job.q data/3prime.fasta.clean.splits/part data/class2/feature

merge_files:
	python merge_feature_file.py data/class1 data/class1_features
	python merge_feature_file.py data/class2 data/class2_features

run_svm:
	cd svm; ./run_svm.sh ../data/class1_features ../data/class2_features

clean:
	rm -rf ./*.log data/*.clean data/*.splits data/class1 data/class2 data/class1_features data/class2_features

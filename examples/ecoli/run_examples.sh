
#collect +/ 20 sequecne of cys
../../scripts/get_align.py ../../databases/sprot-ECOLI-K12.fasta

#extract features
../../scripts/get_feature.py

#svm
svm-predict formated_input ../../models/train_v1.model predict

#formatted result
../../scripts/get_highact.py

# Sequence-Based Prediction of Cysteine Reactivity Using Machine Learning (sbPCR)

## Requirements and Installation

Install libsvm-tools using apt or download libsvm-3.24.tar.gz from https://www.csie.ntu.edu.tw/~cjlin/libsvm/ webpage.

Make sure you can use svm-predict in command line.

## Prediction

Predict high reactivity cysteine using model from our paper (doi:10.1021/acs.biochem.7b00897).

Check run_examples.sh in examples/ecoli/ .

If you have your own fasta need to be predict, simply:

1. Create a new dir in examples/, enter it

2. Collect +/- 20 sequecne of cys

```
../../scripts/get_align.py [fasta]
```

3.  Extract features

```
../../scripts/get_feature.py
```

4. Predict using our model

```
svm-predict formated_input ../../models/train_v1.model predict
```

5. Finalize results

```
../../scripts/get_highact.py
```

## Training your own model

TODO

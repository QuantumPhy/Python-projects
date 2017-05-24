import tensorflow as tf
import numpy as np

# preprocessed data
from datasets.cornell_corpus import data
import data_utils

import importlib
importlib.reload(data)

# load data from pickle and npy files
metadata, idx_q, idx_a = data.load_data(PATH='datasets/cornell_corpus/')
(trainX, trainY), (testX, testY), (validX, validY) = data_utils.split_dataset(idx_q, idx_a)

# parameters 
xseq_len = trainX.shape[-1]
yseq_len = trainY.shape[-1]
batch_size = 16
xvocab_size = len(metadata['idx2w'])  
yvocab_size = xvocab_size
emb_dim = 128
num_units=512
num_heads=16
epochs=100000
min_lr=0.000001
max_lr=0.001
lr_step=5000

import seq2seq_wrapper

importlib.reload(seq2seq_wrapper)
model = seq2seq_wrapper.Seq2Seq(xseq_len=xseq_len,
                               yseq_len=yseq_len,
                               xvocab_size=xvocab_size,
                               yvocab_size=yvocab_size,
                               ckpt_path='ckpt/cornell_corpus/',
                               emb_dim=emb_dim,
                               num_units=num_units,
                               num_heads=num_heads,
                               batch_size=batch_size,
                               epochs=epochs,
                               max_lr=max_lr,
                               min_lr=min_lr,
                               lr_step=lr_step,
                               num_layers=3,
                               )

val_batch_gen = data_utils.rand_batch_gen(validX, validY, batch_size)
test_batch_gen = data_utils.rand_batch_gen(testX, testY, batch_size)
train_batch_gen = data_utils.rand_batch_gen(trainX, trainY, batch_size)

sess = model.train(train_batch_gen, val_batch_gen)

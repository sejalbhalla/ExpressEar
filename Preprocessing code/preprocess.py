import numpy as np
import matplotlib.pyplot as plt
import os

subs = ['s02', 's03', 's06', 's07', 's11', 's12']
for sub in subs:
    fn = 'epoched_data/{}_X.npy'.format(sub)
    X = np.load(fn)
    X1 = X.reshape((X.shape[0], 2, 6, 100))
    # X1 = np.moveaxis(X1, 1, 0)
    X1 = np.moveaxis(X1, 2, -1)
    np.save('preprocessed_data/{}_X.npy'.format(sub), X1)

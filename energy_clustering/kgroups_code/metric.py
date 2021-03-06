"""Metric functions for clustering."""

# Guilherme Franca <guifranca@gmail.com>
# Johns Hopkins University, Neurodata

from __future__ import division

import numpy as np
import scipy.optimize
from sklearn.metrics.cluster import mutual_info_score
from sklearn.metrics.cluster import entropy


def accuracy(z, zh):
    """Compute misclassification error, or better the accuracy which is
    1 - error. Use Hungarian algorithm which is O(n^3) instead
    of O(n!). z and zh are vectors with the dimension
    being the number of points, and each entry is the cluster label assigned
    to that point.

    """
    n, k = len(z), len(np.unique(z))
    m, q = len(zh), len(np.unique(zh))

    assert m == n
    
    Q = np.zeros((n,k))
    for i in range(n):
        Q[i, int(z[i])] = 1
    Qh = np.zeros((n,k))
    for i in range(m):
        Qh[i, int(zh[i])] = 1
    
    cost_matrix = Qh.T.dot(Q)
    row_ind, col_ind = scipy.optimize.linear_sum_assignment(-cost_matrix)
    
    return cost_matrix[row_ind, col_ind].sum()/n

def info_var(z, zh):
    """Compute variation of information based on M. Meila (2007)."""
    return entropy(z) + entropy(zh) - 2*mutual_info_score(z, zh)



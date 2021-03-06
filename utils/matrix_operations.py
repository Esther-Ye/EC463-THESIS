'''
Created on Sep 27, 2019
@author: kwibu
'''
import numpy as np
from functools import reduce
from scipy.sparse import kron as sparse_kron

def matmul(mat_list):
    """
    Compute matrix multiplication of the matrices in mat_list
    
    Arguments: 
    mat_list: list of numpy arrays, the target matrices
    
    Return:
    prod: numpy array, the result
    """
    if len(mat_list) <= 1:
        prod = mat_list[0]
    else:
        prod = reduce(np.matmul, mat_list)
    return prod

def tensor_prod(mat_list, sparse=False):
    """
    Compute tensor product of the matrices in mat_list
    
    Arguments: 
    mat_list: list of numpy arrays, the target matrices
    
    Return:
    prod: numpy array, the result
    """
    
    if len(mat_list) <= 1:
        prod = mat_list[0]
    else:
        prod = reduce(sparse_kron, mat_list) if sparse else reduce(np.kron, mat_list)
    return prod
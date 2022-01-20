"""
Mean-Variance-Standard Deviation Calculator

Function that uses Numpy to output the mean, variance,
standard deviation, max, min, and sum of the rows, columns, and
elements in a 3 x 3 matrix.

Parameters
----------
nine_digits: list[float]
    A List containing exactly nine digits of integers.
    
Returns
-------
dict[str, list]
    A dictionary of lists to output statistical calculations.

Examples
--------
>>> print(calculate([9, 1, 5, 3, 3, 3, 2, 9, 0]))
{
    'mean': [[4.66, 4.33, 2.66], [5.0, 3.0, 3.66], 3.88],
    'variance': [[9.55, 11.55, 4.22], [10.66, 0.0, 14.88], 9.20],
    'standard deviation': [[3.09, 3.39, 2.05], [3.26, 0.0, 3.85], 3.03],
    'max': [[9, 9, 5], [9, 3, 9], 9],
    'min': [[2, 1, 0], [1, 3, 0], 0],
    'sum': [[14, 13, 8], [15, 9, 11], 35]
}
"""


import numpy as np


def calculate(nine_digits: list[float]) -> dict[str, list]:
    if len(nine_digits) != 9:
        raise ValueError('List must contain nine numbers.')
    
    arr = np.array(nine_digits)
    arr = arr.reshape((3, 3))
    out = {}
    
    def append_values(key_: str):
        out[key_] = []
        rows_list = []
        columns_list = []
        
        if key_ == 'mean':
            oper0 = arr.mean(axis=0)
            oper1 = arr.mean(axis=1)
            oper = arr.mean()
        elif key_ == 'variance':
            oper0 = arr.var(axis=0)
            oper1 = arr.var(axis=1)
            oper = arr.var()
        elif key_ == 'standard deviation':
            oper0 = arr.std(axis=0)
            oper1 = arr.std(axis=1)
            oper = arr.std()
        elif key_ == 'max':
            oper0 = arr.max(axis=0)
            oper1 = arr.max(axis=1)
            oper = arr.max()
        elif key_ == 'min':
            oper0 = arr.min(axis=0)
            oper1 = arr.min(axis=1)
            oper = arr.min()
        elif key_ == 'sum':
            oper0 = arr.sum(axis=0)
            oper1 = arr.sum(axis=1)
            oper = arr.sum()

        for e in oper0:
            e = e.item()
            rows_list.append(e)
            
        out[key_].append(rows_list)
        
        for e in oper1:
            e = e.item()
            columns_list.append(e)
            
        out[key_].append(columns_list)
        out[key_].append(oper.item())
    
    append_values('mean')
    append_values('variance')
    append_values('standard deviation')
    append_values('max')
    append_values('min')
    append_values('sum')
    
    return out


# Tests
print('[Test 1] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8')
print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

print('\n[Test 2] Values: 2, 6, 2, 8, 4, 0, 1, 5, 7')
print(calculate([2, 6, 2, 8, 4, 0, 1, 5, 7]))

print('\n[Test 3] Values: 9, 1, 5, 3, 3, 3, 2, 9, 0')
print(calculate([9, 1, 5, 3, 3, 3, 2, 9, 0]))

print('\n[Test 4] Calculate with Few Digits')
# Uncomment to view the exception.
# print(calculate([2, 6, 2, 8, 4, 0, 1]))

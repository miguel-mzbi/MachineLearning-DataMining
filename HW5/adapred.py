# Input: numpy vector alpha of weights, with L rows, 1 column
#        numpy vector theta of feature indices, with L rows, 1 column
#        numpy vector x of d rows, 1 column
# Output: label (+1 or -1)
import numpy as np
def sgn(z):
    if z > 0:
        return 1
    else:
        return -1

def run(alpha,theta,x):
    L, _ = np.shape(alpha)
    summ = 0
    for r in range(L):
        summ += alpha[r]*sgn(x[theta[r]])
    return sgn(summ)
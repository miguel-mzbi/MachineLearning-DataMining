import numpy as np
import K
# Input: number of iterations L
#        numpy matrix X of features, with n rows (samples), d columns (features)
#            X[i,j] is the j-th feature of the i-th sample
#        numpy vector y of labels, with n rows (samples), 1 column
#            y[i] is the label (+1 or -1) of the i-th sample
# Output: numpy vector alpha of n rows, 1 column
def run(L,X,y):

    n, d = X.shape
    alpha = np.zeros((n, 1))
    for iter in range(1, L+1):
        for t in range(0, n):
            sum = 0
            for i in range(0, n):
                sum += alpha[i]*y[i]*K.run(X[i], X[t])
            if y[t]*sum <= 0:
                alpha[t] += 1
    return alpha
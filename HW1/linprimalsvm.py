# Input: numpy matrix X of features, with n rows (samples), d columns (features)
#            X[i,j] is the j-th feature of the i-th sample
#        numpy vector y of labels, with n rows (samples), 1 column
#            y[i] is the label (+1 or -1) of the i-th sample
# Output: numpy vector theta of d rows, 1 column
import numpy as np
import cvxopt as co

def run(X, y):
    n, d = X.shape
    H = np.identity(d);
    f = np.zeros(d);
    A = np.zeros((n, d));
    for i in range(n):
        for j in range(d):
            A[i][j] = -y[i]*X[i][j]
    b = np.full(n, -1)
    theta = np.array(co.solvers.qp(co.matrix(H,tc='d'), co.matrix(f,tc='d'), co.matrix(A,tc='d'), co.matrix(b,tc='d'))['x'])
    return theta
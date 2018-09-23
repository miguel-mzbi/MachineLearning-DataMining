# Input: number of labels k
#        matrix X of features, with n rows (samples), d columns (features)
#            X[i,j] is the j-th feature of the i-th sample
#        vector y of labels, with n rows (samples), 1 column
#            y[i] is the label (1 or 2 ... or k) of the i-th sample
# Output: vector theta of d rows, 1 column
#         vector b of k-1 rows, 1 column
import cvxopt as co
import numpy as np

def sil(yi, l):
    if yi <= (l+1):
        return -1
    else:
        return 1

def run(k,X,y):
    n, d = X.shape
    print X
    print y

    # H
    H = np.block([
        [np.identity(d), np.zeros((d,k-1))],
        [np.zeros((k-1, d)), np.zeros((k-1,k-1))]
    ])
    print "H:\n", H
    
    # f
    f = np.zeros((d+k-1, 1))
    print "f:\n", f
    
    # A
    for m in range(0, n):
        a0 = np.zeros((k-1, d))
        for i in range(0, k-1):
            for j in range(0, d):
                a0[i][j] = -sil(m, i)*X[m][j]
        if m == 0:
            x0 = a0
        else:
            x0 = np.block([
                [x0],
                [a0]
            ])
    x1 = []
    for m in range(0, n):
        a1 = np.zeros((k-1, k-1))
        for i in range(0, k-1):
            for j in range(0, k-1):
                if j == i:
                    a1[i][j] = sil(m, j)
        if m == 0:
            x1 = a1
        else:
            x1 = np.block([
                [x1],
                [a1]
            ])
    x2 = np.zeros((k-2, k-1))
    for i in range(0, k-2):
        for j in range(0, k-1):
            if j == i:
                x2[i][j] = 1
                x2[i][j+1] = -1
    A = np.block([
        [x0, x1],
        [np.zeros((k-2, d)), x2]
    ])
    print "A:\n", A
    
    # c
    c = np.block([
        [np.full((n*(k-1),1), -1)],
        [np.zeros((k-2, 1))]
    ])
    print "c:\n", c

    z = np.array(co.solvers.qp(co.matrix(H,tc='d'),co.matrix(f,tc='d'),co.matrix(A,tc='d'),co.matrix(c,tc='d'))['x'])
    print z
    z = np.split(z.flatten(), [d])
    theta = np.reshape(z[0], (d,1))
    b = np.reshape(z[1], (k-1,1))
    print theta
    print b
    return (theta, b)
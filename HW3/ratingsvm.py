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
    if yi <= l+1:
        return -1
    else:
        return 1

def run(k,X,y):
    print "X:", X
    n, d = X.shape
    H = np.zeros((d+k-1, d+k-1))
    for i in range(d+k-1):
        for j in range(d+k-1):
            if i < d and j < d:
                if i == j:
                    H[i][j] = 1
    print "H:\n", H
    f = np.zeros((d+k-1, 1))
    print "f:\n", f
    A = np.zeros((n*(k-1)+k-2, d+k-1))
    for m in range(1, n+1):
        for i in range((m-1)*(k-1), m*(k-1)):
            for j in range(d):
                A[i][j] = -1*sil(m-1, i%(k-1))*X[m-1][j]
    for m in range(1, n+1):
        for i in range((m-1)*(k-1), m*(k-1)):
            for j in range(d, d+k-1):
                if j-d == i%(k-1):
                    A[i][j] = sil(m-1, j-d)
    for i in range(n*(k-1), n*(k-1)+k-2):
            for j in range(d, d+k-1):
                if j-d == i%(k-1):
                    A[i][j] = 1
                    A[i][j+1] = -1
    print "A:\n", A
    c = np.zeros((n*(k-1)+k-2, 1))
    for i in range(n*(k-1)):
        c[i][0] = -1
    print "c:\n", c
    z = np.array(co.solvers.qp(co.matrix(H,tc='d'),co.matrix(f,tc='d'),co.matrix(A,tc='d'),co.matrix(c,tc='d'))['x'])
    z = np.split(z.flatten(), [d])
    theta = np.reshape(z[0], (d,1))
    b = np.reshape(z[1], (k-1,1))
    print theta
    print b
    return (theta, b)

def main():
    import createsepratingdata
    import ratingpred
    k = 4
    n = 50
    d = 3
    X, y = createsepratingdata.run(n, d, k)
    theta, b = run(k, X, y)
    
    for i in range(n):
        if y[i] == ratingpred.run(k,theta,b,X[i]):
            print y[i], ratingpred.run(k,theta,b,X[i]), True
        else:
            print y[i], ratingpred.run(k,theta,b,X[i]), False

if __name__ == '__main__':
    main()
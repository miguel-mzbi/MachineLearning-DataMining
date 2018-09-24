# Input: number of iterations L
#        number of labels k
#        matrix X of features, with n rows (samples), d columns (features)
#            X[i,j] is the j-th feature of the i-th sample
#        vector y of labels, with n rows (samples), 1 column
#            y[i] is the label (1 or 2 ... or k) of the i-th sample
# Output: vector theta of d rows, 1 column
#         vector b of k-1 rows, 1 column
import numpy as np

def stl(yt, l):
    if yt <= l+1:
        return -1
    else:
        return 1

def run(L,k,X,y):
    n, d = X.shape
    theta = np.zeros((d, 1))
    b = np.zeros((k-1, 1))
    
    for l in range(k-1):
        b[l] = l
    
    for iter in range(1, L+1):
        for t in range(0, n):
            E = set()
            for l in range(k-1):
                condition = stl(y[t], l) * (np.dot(X[t], theta) - b[l])
                if condition <= 0:
                    E.add(l)
            if E:
                summ = 0
                for l in E:
                    summ += stl(y[t], l)
                temp = X[t]
                
                theta += summ*np.reshape(temp, (d, 1))

                for l in E:
                    b[l] -= stl(y[t], l)
    return (theta, b)
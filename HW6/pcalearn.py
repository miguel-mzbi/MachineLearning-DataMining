# Input: number of features F
#        numpy matrix X, with n rows (samples), d columns (features)
# Output: numpy vector mu, with d rows, 1 column
#         numpy matrix Z, with d rows, F columns
import numpy as np
import numpy.linalg as la
def run(F,X):
    n, d = X.shape
    # Calculate average of each feature
    mu = np.zeros((d, 1))
    for i in range(d):
        sigma = 0
        for t in range(n):
            sigma += X[t][i]
        mu[i][0] = (1.0/n)*sigma
    # Substract average to each feature (Now the average is 0)
    for t in range(n):
        for i in range(d):
            X[t][i] = X[t][i] - mu[i]
    # Signular value decomposition
    _, s, Vt = la.svd(X, False)
    # Build g
    g = np.zeros(F)
    for i in range(F):
        g[i] = s[i]
    for i in range(F):
        if(g[i] > 0):
            g[i] = 1.0/g[i]
    # Finalize
    W = np.zeros((F, d))
    for i in range(F):
        W[i] = Vt[i]
    Wt = np.transpose(W)
    g = np.diag(g)
    Z = np.dot(Wt, g)
    Z = np.reshape(Z, (d, F))
    return (mu, Z)
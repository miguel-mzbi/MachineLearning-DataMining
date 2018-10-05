# Input: number of bootstraps B
#        numpy matrix X of features, with n rows (samples), d columns (features)
#        numpy vector y of scalar values, with n rows (samples), 1 column
# Output: numpy vector z of B rows, 1 column
import numpy as np
import linreg
def run(B,X,y):
    n, d = X.shape
    z = np.zeros((B, 1))
    for i in range(B):
        u = [0] * n
        S = set()
        for j in range(n):
            k = np.random.randint(n)
            u[j] = k
            S.add(k)
        
        yU = np.zeros((n, 1))
        XU = np.zeros((n, d))
        for j in range(n):
            yU[j] = y[u[j]]
            XU[j] = X[u[j]]
        
        T = set(range(n)) - S
        thetaHat = linreg.run(XU, yU)

        summ = 0
        for t in T:
            summ += (y[t] - np.dot(X[t], thetaHat))**2
        z[i] = (1.0/len(T))*summ

    return z
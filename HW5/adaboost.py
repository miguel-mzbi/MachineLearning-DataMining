# Input: number of iterations L
#        numpy matrix X of features, with n rows (samples), d columns (features)
#            X[i,j] is the j-th feature of the i-th sample
#        numpy vector y of labels, with n rows (samples), 1 column
#            y[i] is the label (+1 or -1) of the i-th sample
# Output: numpy vector alpha of weights, with L rows, 1 column
#         numpy vector theta of feature indices, with L rows, 1 column
import numpy as np

def sgn(z):
    if z > 0:
        return 1
    else:
        return -1

def run(L,X,y):
    n, d = X.shape
    W = [0]*n
    theta = [0]*L
    alpha = [0]*L
    # Set up uniform weights
    for t in range(n):
        W[t] = 1.0/n
    # Get L features
    for r in range(L):
        epsilon = 0
        first = True
        # Iterate all features in all samples to find best classifier according to W
        for j in range(d):
            summ = 0
            for t in range(n):
                summ += W[t]*y[t]*sgn(X[t][j])
            summ = -1*summ
            # Store error (Epsilon) and the feature that provided that error
            # If error is smaller than the current smaller error
            if(summ < epsilon or first):
                first = False
                epsilon = summ
                theta[r] = j
                print "j", j
                print "theta", theta
        # Get rid of cases close to infinity
        epsilon = np.min([0.99, np.max([-0.99, epsilon])])
        # Compute logodds of epsilon
        alpha[r] = 0.5*np.log((1.0-epsilon)/(1.0+epsilon))
        # Adjust weights
        for t in range(n):
            j = theta[r]
            W[t] = W[t]*np.exp(-1*alpha[r]*y[t]*sgn(X[t][j]))
        # Normalize weights
        weightSum = 0
        for t in range(n):
            weightSum += W[t]
        for t in range(n):
            W[t] = W[t]/weightSum

    alpha = np.reshape(alpha, (L, 1))
    theta = np.reshape(theta, (L, 1))
    return (alpha, theta)
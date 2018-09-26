import linreg
import numpy as np
# Input: number of features F
#        numpy matrix X of features, with n rows (samples), d columns (features)
#            X[i,j] is the j-th feature of the i-th sample
#        numpy vector y of scalar values, with n rows (samples), 1 column
#            y[i] is the scalar value of the i-th sample
# Output: numpy vector of selected features S, with F rows, 1 column
#         numpy vector thetaS, with F rows, 1 column
#             thetaS[0] corresponds to the weight of feature S[0]
#             thetaS[1] corresponds to the weight of feature S[1]
#             and so on and so forth
def run(F,X,y):
    S = set()
    n, d = X.shape
    completeSet = set(range(d))
    
    for f in range(1, F+1):
        
        J = {}
        for j in completeSet-S:
            # Current set to test: S with j
            SJ = S.copy()
            SJ.add(j)
            # Build matrix X with only features in set SJ
            # This will let us do the linear regression with ony those features
            tempX = np.delete(X,list(completeSet-SJ),1)
            # Obtain beta vector (argmin)
            thetaSJ =  linreg.run(tempX, y)
            # Build summatory for the beta vector
            # This will result in min, as the veta vector is the argmin
            summ = 0
            for t in range(n):
                summ += (y[t] - np.dot(tempX[t], thetaSJ))**2
            # Store minimization for this current set
            J[j] = 0.5 * summ
        # Obtain j with bext minimization
        jHat, _ = min(J.items(), key=lambda x:x[1])
        # Adds J to final set S
        S.add(jHat)
    # Build matrix X with only features in final set S
    # This will let us do the linear regression with ony those features
    tempX = np.delete(X,list(completeSet-S),1)
    # Compute linear regresion for final set
    thetaS =  linreg.run(tempX, y)
    # Change S format to numpy vector
    S = np.reshape(list(S), (F, 1))
    return (S, thetaS)
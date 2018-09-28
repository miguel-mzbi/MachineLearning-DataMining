import numpy as np
import linreg
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
    n, d = X.shape
    S = set()
    finalS = []
    completeSet = set(range(d))
    thetaS = np.array([])
    z = np.zeros((n, 1))
    for _ in range(F):
        # Build X matrix for only the features in set S => delete values from complete set - S
        XS = np.delete(X,list(completeSet-S),1)
        for t in range(n):
            dot = np.dot(XS[t], thetaS)
            z[t] = y[t] - dot
        
        J = {}
        for j in completeSet-S:
            summ = 0
            for t in range(n):
                summ += (z[t]*X[t][j])
            # Store minimization for this current set
            J[j] = -summ[0]
            #print "j candidate", j, "->", -summ[0]
        
        # Obtain j with bext minimization (And its corresponding thetaJ)
        jHat, _ = max(J.items(), key=lambda x:x[1])
        # print "MAX ", jHat
        # Compute weight for selected jHat
        thetaJ = linreg.run(np.reshape(X[:,jHat], (n,1)), z)
        # print "maxTheta", thetaJ
        # Constructs final thetaS
        if len(thetaS) == 0:
            thetaS = thetaJ
        else:
            thetaS = np.block([
                [thetaS],
                [thetaJ]
            ])
        #print "thetaS", thetaS
        # Adds J to final set S
        S.add(jHat)
        finalS.append(jHat)
        
    # Reshape set as numpy list
    S = np.reshape(finalS, (F, 1))
    return (S, thetaS)
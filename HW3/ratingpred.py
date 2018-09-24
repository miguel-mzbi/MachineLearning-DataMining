# Input: number of labels k
#        vector theta of d rows, 1 column
#        vector b of k-1 rows, 1 column
#        vector x of d rows, 1 column
# Output: label (1 or 2 ... or k)
import numpy as np
def run(k, theta, b, x):
    thetaX = np.dot(x, theta)
    for l in range(0, k):
        if l == 0:
            if thetaX <= b[l]:
                return l+1
        elif l == k-1:
            if b[l-1] < thetaX:
                return l+1
        else:
            if b[l-1] < thetaX and thetaX <= b[l]:
                return l+1

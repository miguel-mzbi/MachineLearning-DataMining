def main():
    import createsepratingdata
    import ratingpred
    import ratingprank
    import ratingsvm
    import numpy as np
    L = 400
    n = 10
    d = 6
    k = 6
    X, y = createsepratingdata.run(n, d, k)

    print X
    print y

    thetaA, bA = ratingprank.run(L, k, X, y)
    print "----------------"
    print thetaA
    print bA

    thetaB, bB = ratingsvm.run(k, X, y)
    
    print "y\tPRank\tSVM"
    for i in range(n):
        print y[i], "\t", ratingpred.run(k,thetaA,bA,X[i]), "\t", ratingpred.run(k,thetaB,bB,X[i])

if __name__ == '__main__':
    main()
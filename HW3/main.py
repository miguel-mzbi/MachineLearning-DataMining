def main():
    import createsepratingdata
    import ratingpred
    import ratingprank
    import ratingsvm
    import numpy as np
    L = 300
    n = 3
    d = 2
    k = 3
    X, y = createsepratingdata.run(n, d, k)

    print X
    print y

    thetaA, bA = ratingprank.run(L, k, X, y)
    thetaB, bB = ratingsvm.run(k, X, y)
    
    print "y\tPRank\tSVM"
    for i in range(n):
        print y[i], "\t", ratingpred.run(k,thetaA,bA,X[i]), "\t", ratingpred.run(k,thetaB,bB,X[i])

if __name__ == '__main__':
    main()
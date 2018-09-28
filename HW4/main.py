def main():
    import createlinregdata
    import greedysubset
    import forwardfitting
    import time

    n = 10
    d = 4
    F = 2

    X, y = createlinregdata.run(n, d)
    # print "X: ", X
    # print "y: ", y
    start = time.time()
    greedyS, greedyTheta = greedysubset.run(F, X, y)
    end = time.time()
    print "Elapsed time: ", end - start
    print "greedyS: ", greedyS
    print "greedyTheta: ", greedyTheta
    
    start = time.time()
    forwardS, forwardTheta = forwardfitting.run(F, X, y)
    end = time.time()
    print "Elapsed time: ", end - start
    print "forwardS: ", forwardS
    print "forwardTheta: ", forwardTheta

if __name__ == '__main__':
    main()
def main():
    import createlinregdata
    import greedysubset
    import forwardfitting
    import myopicfitting
    import time

    n = 10
    d = 5
    F = 4

    X, y = createlinregdata.run(n, d)
    # print "X: ", X
    # print "y: ", y
    start = time.time()
    greedyS, greedyTheta = greedysubset.run(F, X, y)
    end = time.time()
    print "Elapsed time: ", end - start
    print "greedyS: ", greedyS
    print "greedyTheta: ", greedyTheta
    
    print "\n~~~~~~~~~~~~~~~~~~~~~\n"

    start = time.time()
    forwardS, forwardTheta = forwardfitting.run(F, X, y)
    end = time.time()
    print "Elapsed time: ", end - start
    print "forwardS: ", forwardS
    print "forwardTheta: ", forwardTheta
    
    print "\n~~~~~~~~~~~~~~~~~~~~~\n"

    start = time.time()
    myopicS, myopicTheta = myopicfitting.run(F, X, y)
    end = time.time()
    print "Elapsed time: ", end - start
    print "myopicS: ", myopicS
    print "myopicTheta: ", myopicTheta

if __name__ == '__main__':
    main()
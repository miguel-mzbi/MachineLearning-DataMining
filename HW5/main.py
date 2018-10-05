def main():
    import numpy as np
    import createsepdata
    import createlinregdata
    import adaboost
    import adapred
    n = 20
    d = 2
    L = 10

    sepX, sepy = createsepdata.run(n, d)
    # print "sepX", sepX
    # print "sepy", sepy

    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    adaBoostAlpha, adaBoostTheta = adaboost.run(L, sepX, sepy)
    # print adaBoostAlpha
    # print adaBoostTheta
    correct = 0
    for i in range(n):
        pred = adapred.run(adaBoostAlpha, adaBoostTheta, np.reshape(sepX[i], (d, 1)))
        if sepy[i] == pred:
            correct += 1
        # print sepy[i][0], pred, sepy[i] == pred
    print "AdaBoost Accuracy = ", correct*(1.0)/n

    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    linX, liny = createlinregdata.run(n, d)
    # print "sepX", linX
    # print "sepy", liny

if __name__ == '__main__':
    main()
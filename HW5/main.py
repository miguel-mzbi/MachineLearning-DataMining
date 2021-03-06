def main():
    import numpy as np
    import createsepdata
    import createlinregdata
    import adaboost
    import adapred
    import kfoldcv
    import bootstrapping
    n = 10
    d = 3
    L = 10
    k = 5
    B = 5

    sepX, sepy = createsepdata.run(n, d)
    # print "sepX", sepX
    # print "sepy", sepy

    print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    adaBoostAlpha, adaBoostTheta = adaboost.run(L, sepX, sepy)
    print adaBoostAlpha
    print adaBoostTheta
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
    kfoldZ = kfoldcv.run(k, linX, liny)
    print kfoldZ
    bootZ= bootstrapping.run(B, linX, liny)
    print bootZ

if __name__ == '__main__':
    main()
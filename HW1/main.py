def main():
    import linepred
    import createsepdata
    import linperceptron
    import linprimalsvm
    L = 10
    n = 7
    d = 5

    X, y = createsepdata.run(n, d)

    thetaA = linperceptron.run(L, X, y)
    thetaB = linprimalsvm.run(X, y)
    
    print "\nTHETA Perceptron\n", thetaA
    for i in range(n):
        if(y[i] == linepred.run(thetaA, X[i])):
            print True
        else:
            print False
    print "\nTHETA SVM\n", thetaB
    for i in range(n):
        if(y[i] == linepred.run(thetaB, X[i])):
            print True
        else:
            print False
    

if __name__ == '__main__':
    main()
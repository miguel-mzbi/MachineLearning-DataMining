def main():
    import kerpred
    import createsepdata
    import kerperceptron
    import kerdualsvm
    L = 10
    n = 7
    d = 5

    X, y = createsepdata.run(n, d)
    print X, y

    alphaA = kerperceptron.run(L, X, y)
    alphaB = kerdualsvm.run(X, y)
    
    print "\nTHETA Perceptron\n", alphaA
    for i in range(n):
        if(y[i] == kerpred.run(alphaA, X, y, X[i])):
            print True
        else:
            print False
    print "\nTHETA SVM\n", alphaB
    for i in range(n):
        if(y[i] == kerpred.run(alphaB, X, y, X[i])):
            print True
        else:
            print False
    

if __name__ == '__main__':
    main()
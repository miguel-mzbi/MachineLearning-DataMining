def main():
    import pcalearn
    import pcaproj
    import numpy as np
    
    F = 1

    np.set_printoptions(precision=4)
    X = np.array([
        [-3, 2],
        [-2, 1.5],
        [-1, 1],
        [0, 0.5],
        [1, 0]
    ])
    XTest = np.array([
        [-3, 2],
        [-2, 1.5],
        [-1, 1],
        [0, 0.5],
        [1, 0]
    ])

    mu, Z = pcalearn.run(F, X)
    print "mu:", mu
    print "Z:", Z

    PTest = pcaproj.run(XTest, mu, Z)
    print "PTest", PTest

if __name__ == '__main__':
    main()
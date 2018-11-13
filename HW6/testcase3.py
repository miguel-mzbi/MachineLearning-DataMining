def main():
    import pcalearn
    import pcaproj
    import numpy as np
    
    F = 3

    np.set_printoptions(precision=4)
    X = np.array([
        [-2, 2, 0, -2, 2, 0, 4],
        [-3, -1.5, -2, 6, 5, 1, 4],
        [-1, 1, 4, 0, 5, -4, 5],
        [1, -0.5, 5, -9, -9, 0, 0],
        [2, 0, -2, -4.5, 3, 3, 1]
    ])
    XTest = np.array([
        [-4, 5, 1, -4, -4, 0, 1],
        [2, 1, 4, -9.5, -4, 0, 1]
    ])

    mu, Z = pcalearn.run(F, X)
    print(mu)
    print(Z)

    PTest = pcaproj.run(XTest, mu, Z)
    print(PTest)

if __name__ == '__main__':
    main()
def main():
    import pcalearn
    import pcaproj
    import numpy as np
    
    F = 2

    np.set_printoptions(precision=4)
    X = np.array([
        [-2, 2, 0],
        [-3, -1.5, -2],
        [-1, 1, 4],
        [1, -0.5, 5],
        [2, 0, -2]
    ])
    XTest = np.array([
        [-4, 5, 1],
        [2, 1, 4],
        [-4, 5, 7.5],
        [-9.5, 0, 0]
    ])

    mu, Z = pcalearn.run(F, X)
    print(mu)
    print(Z)

    PTest = pcaproj.run(XTest, mu, Z)
    print(PTest)

if __name__ == '__main__':
    main()
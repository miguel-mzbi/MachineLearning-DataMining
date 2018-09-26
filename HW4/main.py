def main():
    import createlinregdata
    import greedysubset

    n = 5
    d = 4
    F = 3

    X, y = createlinregdata.run(n, d)
    print X
    print y

    greedyS, greedyTheta = greedysubset.run(F, X, y)

    print greedyS
    print greedyTheta

if __name__ == '__main__':
    main()
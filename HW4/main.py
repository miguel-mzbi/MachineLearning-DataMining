def main():
    import createlinregdata
    import linreg

    n = 3
    d = 1

    X, y = createlinregdata.run(n, d)
    print X
    print y
    thetaHat = linreg.run(X, y)
    print thetaHat

if __name__ == '__main__':
    main()
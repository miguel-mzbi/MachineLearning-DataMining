def main():
    import createsepdata
    import createlinregdata
    n = 10
    d = 5

    sepX, sepy = createsepdata.run(n, d)
    print "sepX", sepX
    print "sepy", sepy

    linX, liny = createlinregdata.run(n, d)
    print "sepX", linX
    print "sepy", liny

if __name__ == '__main__':
    main()
fh = open('FF_tiny.txt')

lines = fh.readlines()

for line in lines:
    firstcol = line.split()[0]
    seccol = line.split()[1]
    thirdcol = line.split()[2]
    fourcol = line.split()[3]
    lastcol = line.split()[-1]
    year = firstcol[:4]
    yearformatted = int(year)
    if yearformatted > 1927:
        print(yearformatted,seccol, thirdcol,fourcol, lastcol)


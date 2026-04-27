fh = open('FF_tiny.txt')

def sorted_by_last(line):
    parts = line.rstrip().split()
    return float(parts[-1])

right_order = sorted(fh, key= sorted_by_last)


for line in right_order:
    print(line.rstrip())
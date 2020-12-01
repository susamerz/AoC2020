numbers = set()
with open('Report.csv') as fi:
    for line in fi:
        numbers.add(int(line.strip(' ')))
    fi.close()

for n in numbers:
    test = 2020 - n
    if (test in numbers):
        target = test
res = target * (2020-target)
print(res)

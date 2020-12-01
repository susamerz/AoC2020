numbers = set()
with open('Report.csv') as fi:
    for line in fi:
        numbers.add(int(line.strip(' ')))
    fi.close()
sorted_numbers = sorted(numbers)
smallest=sorted_numbers[0]
for n in reversed(sorted_numbers):
    test1 = 2020 - n
    for m in sorted_numbers:
        test2=test1-m
        if (test2 < smallest):
            break
        if (test2 in numbers):
            target1 = test2
            target2 = m
            target3 = n
res = target1 * target2 * target3
print(res)



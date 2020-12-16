#starting = [0,3,6] # test output, solution should be 436
starting = [2, 0, 6, 12, 1, 3]

spoken = dict()
for i in starting[:-1]:
    spoken[i]=starting.index(i)
num = starting[-1]
for i in range(len(starting)-1,29999999):
    if num in spoken:
        next_num = i- spoken[num]
        spoken[num] = i
        num = next_num
    else:
        spoken[num] = i
        num = 0

print(f'solution is {num}')
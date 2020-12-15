#starting = [0,3,6] # test output, solution should be 436
starting = [2, 0, 6, 12, 1, 3]

def next_number(prev_sequence):
    sub_sequence = prev_sequence[0:-1]
    if not prev_sequence[-1] in sub_sequence:
        return(0)
    else:
        sub_sequence.reverse()
        dist_to_last = sub_sequence.index(prev_sequence[-1])
        return dist_to_last+1


spoken = starting.copy()
for i in range(len(starting),30000000):
    num = next_number(spoken)
    spoken.append(num)
print(f'solution 1 is {spoken[29999999]}')
import numpy as np

with open('input_D10') as fi:
    in_list = [int(i) for i in fi.readlines()]
    in_list = sorted(in_list)
    step_counter = np.zeros(3, dtype=int)
    previous = 0
    for i in in_list:
        step_counter[(i-previous)-1]+=1
        previous = i
    step_counter[2]+=1  # final adapter built into device, i.e. not in the list
    print(f"solution part 1 is {step_counter[0]*step_counter[2]}")

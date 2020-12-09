def update_lookup(lookup_list, new_element, old_data):
    #print(old_data)
    del lookup_list[0]
    new_set = set()
    for i,old_set in zip(old_data,lookup_list):
        if new_element != i: old_set.add(new_element+i)
    lookup_list.append(new_set)
    return lookup_list


def compute_lookup(initial_list):
    lookup_list=list()
    for i,value1 in enumerate(initial_list):
        curr_set = set()
        for value2 in initial_list[i+1:]:
            if value1 != value2: curr_set.add(value1+value2)
        lookup_list.append(curr_set)
    return lookup_list



preamble_length = 25
with open('input_D9') as fi:
    data = [int(i) for i in fi.readlines()]
    lookup_list = compute_lookup(data[0:preamble_length])
    for i in range(preamble_length, len(data)):
        #print(lookup_list)
        curr_value = data[i]
        #print(curr_value)
        if not any(curr_value in l for l in lookup_list):
            solution1=curr_value
            print(f"part1 solution is {curr_value}")
            break
        else: update_lookup(lookup_list,curr_value, data[(i-preamble_length)+1:i])
    for i in range(0, len(data)):
        summed = 0
        j = i
        while summed < solution1:
            summed += data[j]
            j += 1
        if (summed == solution1):
            print(f"solution 2 is {min(data[i:j])+ max(data[i:j])}")
            break
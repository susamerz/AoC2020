import re
counter = 0
counter_part2 = 0
with open('input2') as fi:
    for line in fi:
        (conditions, passwd) = line.split(':')
        (numbers, testchar)=conditions.split(' ')
        (lower,upper)= numbers.split("-")
        if((passwd[int(lower)]==testchar) ^ (passwd[int(upper)]==testchar)):
            counter_part2 = counter_part2+1
        numchars = re.findall(testchar,passwd)
        if(len(numchars)<int(lower) or len(numchars) >int(upper)):
            continue
        counter= counter+1
    print(f"first part result is {counter}")
    print(f"second part result is {counter_part2}")
    fi.close()

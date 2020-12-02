import re
counter=0
with open('input2') as fi:
    for line in fi:
        (conditions, passwd) = line.split(':')
        (numbers, testchar)=conditions.split(' ')
        (lower,upper)= numbers.split("-")
        numchars = re.findall(testchar,passwd)
        if(len(numchars)<int(lower) or len(numchars) >int(upper)):
            continue
        counter= counter+1
    print(counter)
    fi.close()
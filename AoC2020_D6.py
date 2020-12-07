import string
with open("input_D6") as fi:
    txt = fi.read()
    answers_by_group = txt.split('\n\n')
    out1 = 0
    out2=0
    for ex in answers_by_group:
        ex = ex.strip('\n')
        part1=ex.replace('\n', '')
        part1=set(part1)
        out1 += len(part1)
        matching = set(string.ascii_lowercase)
        for person in ex.split('\n'):
            person = set(person)
            matching = matching.intersection(person)
        out2 += len(matching)

    print(f"part one result is {out1}")
    print(f"part two result is {out2}")
def check_passport(pp):
    # check if the dict pp contains all fields required, if yes return 1, else 0
    is_valid=1
    print(pp)
    required_fields=('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for field in required_fields:
        if (not field in pp):
            is_valid = 0
            break
    return is_valid


current_passport = dict()
valids=0
with open('input_D4')as fi:
    for line in fi:
        if (line == "\n" or line == "eof"):
            valids += check_passport(current_passport)
            current_passport = dict()
        else:
            new_entries = line.split(' ')
            for e in new_entries:
                (key, value) = e.split(":")
                current_passport[key] = value
    valids+= check_passport(current_passport)
print(valids)

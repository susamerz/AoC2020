import re
def check_passport(pp):
    # check if the dict pp contains all fields required, if yes return 1, else 0
    is_valid=0
    #print(pp)
    required_fields=('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for field in required_fields:
        if (not field in pp):
            return is_valid
    height_unit = re.findall('cm$|in$', pp['hgt'])
    height_value = int(re.findall('\d*', pp['hgt'])[0])
    if  len(re.findall('^(\d){4}$',pp['byr'])) != 1:
        return is_valid
    if int(pp["byr"])<1920 or int(pp["byr"])> 2002:
        return is_valid
    if  len(re.findall('^(\d){4}$',pp['iyr'])) != 1:
        return is_valid
    if int(pp['iyr'])<2010 or int(pp['iyr'])>2020:
        return is_valid
    if len(re.findall('^(\d){4}$', pp['eyr'])) != 1:
        return is_valid
    if int(pp['eyr'])<2020 or int(pp['eyr'])>2030:
        return is_valid
    if len(height_unit) != 1:
        return is_valid
    if height_unit[0] == "cm" and (height_value<150 or height_value>193):
        return is_valid
    if height_unit[0] == "in"and (height_value<59 or height_value>76):
        return is_valid
    if len(re.findall('^#[0-9a-f]{6}$' ,pp['hcl'])) != 1:
        return is_valid
    if len(re.findall('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$',pp['ecl'])) != 1:
        return is_valid
    if len(re.findall('^[0-9]{9}$', pp['pid'])) != 1:
        return is_valid
    print(pp)
    is_valid = 1
    return is_valid



current_passport = dict()
valids=0
with open('input_D4')as fi:
    for line in fi:
        if (line == "\n"):
            valids += check_passport(current_passport)
            current_passport = dict()
        else:
            new_entries = line.split(' ')
            for e in new_entries:
                (key, value) = e.split(":")
                current_passport[key] = value
    valids+= check_passport(current_passport)
print(valids)

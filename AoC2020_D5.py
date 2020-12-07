# compute the checks
def compute_seat_id(seat_string):
    row_string = parse_to_binary(seat_string[0:7])
    row_number = int(row_string,base=2)
    col_string = parse_to_binary(seat_string[7:-1])
    print(col_string)
    col_number = int(col_string,base=2)
    print(col_number)
    return row_number*8 + col_number

def parse_to_binary(sub_string):
    letter_to_number_map = dict({'F': '0', 'B': '1','R':'1','L':'0'})
    out = list()
    for c in sub_string:
        out.append(letter_to_number_map[c])
    return ''.join(out)

with open("input_D5") as fi:
    max_id=0
    for line in fi:
        curr_id = compute_seat_id(line)
        if curr_id > max_id:
            max_id=curr_id
    print(f" maximum checksum found is: {max_id}")

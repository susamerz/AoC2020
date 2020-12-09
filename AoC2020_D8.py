with open('input_D8') as fi:
    in_program = fi.readlines()
    visited_lines = set()
    curr_line = 0
    acc = 0
    while not curr_line in visited_lines:
        curr_instruct = in_program[curr_line]
        op, arg = curr_instruct.split(' ')
        visited_lines.add(curr_line)
        if op == 'nop':
            curr_line +=1
            continue
        if op == 'acc':
            acc += int(arg)
            curr_line +=1
            continue
        if op == 'jmp':
            curr_line += int(arg)
    print(f"part 1 : {acc}")

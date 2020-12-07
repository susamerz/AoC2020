import re

def count_bags(node_name):
    curr_node = baggage_rules[node_name]
    out = 0
    if 'other' in curr_node:
        return 0
    for c,num in curr_node.items():
        out += count_bags(c) * int(num) + int(num)
    return out


with open('input_D7') as fi:
    baggage_rules = dict()
    for line in fi:
        entry = line.split('contain')
        key = re.sub('bags', '', entry[0]).strip()
        vals = re.sub(' bags| bag', '', entry[1]).strip('. \n')
        vals = vals.split(', ')
        values = dict()
        for v in vals:
            num, color = v.split(' ', maxsplit=1)
            values[color] = num
        baggage_rules[key]=values
    #print(baggage_rules)

    bag_colors = set()
    new_colors = {'shiny gold'}
    while len(new_colors)>0:
        current_cols = new_colors
        new_colors = set()
        for c in current_cols:
            for node, children in baggage_rules.items():
                children = set(children)
                if c in children:
                    if not c in bag_colors:
                        new_colors.add(node)
        bag_colors = bag_colors.union(current_cols)
    print(f"part1 is {len(bag_colors)-1}")

    # assuming that there is no circularity in the subtree we are traversing,
    # because otherwise this will go, well you know where
    root_col = 'shiny gold'
    num_bags= count_bags(root_col)

    print(f"part2 is {num_bags}")




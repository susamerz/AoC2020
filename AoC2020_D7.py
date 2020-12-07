import re
with open('input_D7') as fi:
    baggage_rules = dict()
    for line in fi:
        entry = line.split('contain')
        key = re.sub('bags+', '', entry[0]).strip()
        vals = re.sub('\d | bags| bag','',entry[1]).strip('. \n')
        vals = vals.split(', ')
        baggage_rules[key]=set(vals)
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


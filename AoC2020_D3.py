import numpy as np

## code bit for converter provided by Marijn van Vliet
to_tree_or_not_to_tree = lambda s: 1 if s == b'#' else 0
converters = {i:to_tree_or_not_to_tree for i in range(31)}

input = np.genfromtxt("input_AoC2020_D3", delimiter=1, converters=converters,dtype=int,comments=None)


def count_trees(xslope,yslope):
    global output
    linecounter = 0
    colcounter = 0
    output = 0
    while linecounter < input.shape[0]:
        output += input[linecounter, colcounter % 31]
        colcounter += yslope
        linecounter += xslope
    return output


out1 = count_trees(1,3)
out2 = count_trees(1,1)
out3 = count_trees(1,5)
out4 = count_trees(1,7)
out5 = count_trees(2,1)

out_part2=out1*out2*out3*out4*out5
print(f"result part 1 is {out1}")
print(f"result part2 is {out_part2}")
import re
def my_map(in_file):
    temperature = dict()
    for line in in_file:
        pairs=line.split()
        temp=pairs[0][2:4]
        if(temp in temperature):
            temperature[temp].append(pairs[1])
        else:
            temperature[temp]=[pairs[1]]
    return temperature
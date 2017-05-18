import sys
import my_map
import my_reduce

key_value = dict()
for filename in ['data_2010.txt', 'data_2011.txt', 'data_2012.txt', 'data_2013.txt', 'data_2014.txt', 'data_2015.txt']:
    in_file = open(filename, 'r')
    key_value_per_file = my_map.my_map(in_file)
    for key in key_value_per_file:
        if(key in key_value):
            key_value[key].append(key_value_per_file[key])
        else:
            key_value[key]=[key_value_per_file[key]]
reduced = dict()
for key in key_value:
    reduced[key] = my_reduce.my_reduce(key_value[key])
for key in reduced:
    print(key + ": " + str(reduced[key]))

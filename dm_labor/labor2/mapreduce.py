import sys
import my_map
import my_reduce

key_value = dict()
for filename in ['raven_01.txt', 'raven_02.txt', 'raven_03.txt']:
    if(filename != sys.argv[0]):
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

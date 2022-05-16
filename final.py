import os
from itertools import islice

os.chdir('/home/azhar/Desktop/Testing')

rows = 5
shift = False

max_values_per_position = {}
min_values_per_position = {}
average_values_per_position = {}


'''
085-59141D-066-1C1E09-06704842510039E0
position 3, 9 with pair which is 59141D
59 -> a
14 -> b
1D -> c
'''
fromPosition = 3
toPosition = 9
position = ['a', 'b', 'c']


def get_min_max_mean_of_hex(filename, from_rows=1, to_rows=1000, shift=False):
    max_values_per_position = {}
    min_values_per_position = {}
    summed_value_per_position = {}

    with open(filename, 'r') as file:
        for line in islice(file, from_rows, to_rows+1):
            data = (line.strip())
            if shift:
                data = data[1:][fromPosition:toPosition]
            else:
                data = ('0' + data)[fromPosition+2:toPosition+2]

            for x in range(0, len(data), 2):
                y = [int(data[x]+data[x+1], 16)
                     for x in range(0, len(data)-1, 2)]

            for index, j in enumerate(y):
                if not (max_values_per_position.get(position[index])):
                    max_values_per_position[position[index]] = j
                    min_values_per_position[position[index]] = j
                    summed_value_per_position[position[index]] = j
                else:
                    max_values_per_position[position[index]] = (j if max_values_per_position.get(position[index]) < j
                                                                else max_values_per_position.get(position[index]))
                    min_values_per_position[position[index]] = (j if min_values_per_position.get(position[index]) > j
                                                                else min_values_per_position.get(position[index]))
                    summed_value_per_position[position[index]] = (
                        summed_value_per_position.get(position[index]) + j)

        mean = ({position[index]: round((summed_value_per_position.get(key)/len(data)), 2)
                for index, key in enumerate(summed_value_per_position)})

    return {"max": max_values_per_position, "min": min_values_per_position, "average": mean}


print(get_min_max_mean_of_hex("file1.csv"))
# print(get_min_max_mean_of_hex("file1.csv", 1, 5, True))
# print(get_min_max_mean_of_hex("file1.csv", 6, 10, False))
# print(get_min_max_mean_of_hex("file1.csv", 11, 15, False))
# print(get_min_max_mean_of_hex("file1.csv", 16, 20, False))
# print(get_min_max_mean_of_hex("file1.csv", 21, 25, False))

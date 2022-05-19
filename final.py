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


print(get_min_max_mean_of_hex("file1.csv", 1, 5, True))
print(get_min_max_mean_of_hex("file1.csv", 6, 10, False))
print(get_min_max_mean_of_hex("file1.csv", 11, 15, False))
print(get_min_max_mean_of_hex("file1.csv", 16, 20, False))
print(get_min_max_mean_of_hex("file1.csv", 21, 25, False))
'''
#output
{'max': {'a': 89, 'b': 55, 'c': 27}, 'min': {'a': 87, 'b': 8, 'c': 1}, 'average': {'a': 73.33, 'b': 24.67, 'c': 14.33}}
{'max': {'a': 89, 'b': 35, 'c': 47}, 'min': {'a': 88, 'b': 10, 'c': 12}, 'average': {'a': 73.5, 'b': 16.33, 'c': 24.33}}
{'max': {'a': 89, 'b': 22, 'c': 56}, 'min': {'a': 87, 'b': 8, 'c': 9}, 'average': {'a': 73.33, 'b': 12.0, 'c': 28.5}}
{'max': {'a': 88, 'b': 57, 'c': 57}, 'min': {'a': 88, 'b': 6, 'c': 7}, 'average': {'a': 73.33, 'b': 31.0, 'c': 29.17}}
{'max': {'a': 89, 'b': 51, 'c': 45}, 'min': {'a': 87, 'b': 8, 'c': 0}, 'average': {'a': 73.67, 'b': 22.17, 'c': 21.83}}
'''
print(get_min_max_mean_of_hex("file1.csv"))
# {'max': {'a': 89, 'b': 57, 'c': 57}, 'min': {'a': 87, 'b': 6, 'c': 0}, 'average': {'a': 382.0, 'b': 111.33, 'c': 119.83}}


# date is getting different for different position
from_index = 2
to_index = -2
def get_date_time(filename, from_rows=0, to_rows=1000):
    def convert(x):
        return datetime.utcfromtimestamp(eval("0x" + x[from_index:to_index]))

    with open(filename) as file:
        for line in islice(file, from_rows, to_rows+1):
            data = (line.strip())

            data = data[data.rfind('-')+2:][:12]
            print(convert(data))


get_date_time("file1.csv")


# getting lat and long
shift = False
from_index = 4
to_index = 9
with open('file1.csv') as file:
    for line in islice(file, 0, 6):
        data = line.strip()
        if shift:
            lat_hex = data[1:][3:9]
            long_hex = data[1:][14:20]
        else:
            lat_hex = ('0'+data)[5:11]
            long_hex = ('0'+data)[16:22]

        lat_hex = int(lat_hex, 16)/1e5
        long_hex = int(long_hex, 16)/1e5

        print(lat_hex, long_hex)

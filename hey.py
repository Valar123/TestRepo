data = [
'85-59141D-066-1C1E09-06704842510039E0',
'85-583201-096-1D0C08-067038382300AABE',
'85-580813-016-1C2100-087048427600DBAF',
'85-591B0E-056-1D1833-0870483866007242'
]

max_values_per_position = {}
min_values_per_position = {}
average_values_per_position = {}

# position 3, 9 with pair
index1 = 3
index2 = 9 

# this will be dynamic
position = ['34', '56', '78']

for i in data:
    hex_1 = i[index1:index2]
    for x in range(0, len(i[index1:index2]), 2):
        y = [int(hex_1[x]+hex_1[x+1] ,16) for x in range(0, len(i[index1:index2])-1, 2)]
    
    
    for index, j in enumerate(y):
        if not (max_values_per_position.get(position[index])):
            max_values_per_position[position[index]] = j
            min_values_per_position[position[index]] = j
            average_values_per_position[position[index]] = j
        else:
            max_values_per_position[position[index]] = j if max_values_per_position.get(position[index]) < j else max_values_per_position.get(position[index])
            min_values_per_position[position[index]] = j if min_values_per_position.get(position[index]) > j else min_values_per_position.get(position[index])
            average_values_per_position[position[index]] = (average_values_per_position.get(position[index]) + j)
    
    mean =  ({position[index]:(average_values_per_position.get(key)/len(data)) 
                                    for index, key in enumerate(average_values_per_position)})

print(max_values_per_position)
# {'34': 89, '56': 50, '78': 29}
# for position (34) we have max value 89, for 5&6 position we have max value 50 ....
print(min_values_per_position)
# {'34': 88, '56': 8, '78': 1}
## for position 3&4 we have min value 88 ............
print(mean)
# {'34': 88.5, '56': 26.25, '78': 15.75}


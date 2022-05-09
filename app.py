import os
import datetime
import shutil
from shutil import copytree, ignore_patterns
from ast import literal_eval
from itertools import islice
import json

# import usb.core
# import usb.util

# dev = usb.core.find(idVendor= 0x0781, idProduct=0x5567)

# ep = dev[0].interfaces()[0].endpoints()[0]
# i=dev[0].interfaces()[0].bInterfaceNumber
# dev.reset()

# if dev.is_kernel_driver_active(i):
#     dev.detach_kernel_driver(i)


# dev.set_configuration()
# eaddr = ep.bEndpointAddress

# r = dev.read(eaddr, 1024)

# print(len(r))
# print('working uptill now ')


import os

os.chdir('/home/azhar/Desktop/Testing')



shift = True  # 0 if shift to left else right
rows = 20 # all data selected from a file
selected_file_name = 'file1.csv' # selected from a folder
dict_describe = {'min':{}, 'max':{}, 'mean':{}}


with open(selected_file_name, 'r') as file:
    filename, file_extension = os.path.splitext(selected_file_name)
    if (file_extension in [".csv", ".xls", ".xlxs"]):
        
        # looping over n rows 
        for line in islice(file,1, rows):
            data = (line.strip().split(',')[1])
            data = data[0:data.rindex('-')].split('-')

            # conversion hexa to deci
            data[1] = int(data[1], 16)
            data[3] = int(data[3], 16)
            if shift:
                data[0], data[1], data[2], data[3] = data[1], data[0], data[3], data[2]

            # pairing
            pair = [(data[x], data[x+1]) for x in range(0, len(data), 2)]

            # getting min, max, average on position
            for x,y in pair:
                if y not in dict_describe['max']:
                    dict_describe['max'][y] = x
                    dict_describe['min'][y] = x
                    dict_describe['mean'][y] = x
                else:
                    dict_describe['max'][y] = (x if dict_describe['max'].get(y) < x 
                                                else dict_describe['max'].get(y))

                    dict_describe['min'][y] = (x if dict_describe['min'].get(y) > x 
                                                else dict_describe['min'].get(y))

                    dict_describe['mean'][y] = (x + dict_describe['mean'].get(y)) // 2

    else:
        print('wrong format')


# point 6
# should I create a filter function so that user can filter out the result (on basis of lat/long) 
with open('export.py', 'w') as f:
    f.write(json.dumps(dict_describe))

# {'min': {'085': 5703707, '066': 1842697, '096': 1838081, '016': 1775902, '056': 1776174, '036': 1841165, '046': 1840143, '086': 1844487, '076': 1841703, '006': 1908754, '026': 1908500}, 
#  'max': {'085': 5839630, '066': 1842697, '096': 1908754, '016': 1907215, '056': 1906739, '036': 1841165, '046': 1840143, '086': 1844487, '076': 1841703, '006': 1909038, '026': 1908500},
#  'mean': {'085': 5771286.408401489, '066': 1842697, '096': 1881612.5, '016': 1825747.125, '056': 1839923.25, '036': 1841165, '046': 1840143, '086': 1844487, '076': 1841703, '006': 1908896.0, '026': 1908500}}
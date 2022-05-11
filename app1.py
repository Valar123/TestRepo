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



shift = False 
rows = 6 # all data selected from a file
selected_file_name = 'file1.csv' # selected from a folder
dict_describe = {'max':[], 'min':[], 'mean':[]}
params = {'lat':[], 'long':[]}

with open(selected_file_name, 'r') as file:
    filename, file_extension = os.path.splitext(selected_file_name)
    if (file_extension in [".csv", ".xls", ".xlxs"]):
        
        # looping over n rows 
        for line in islice(file,1, rows):
            data = (line.strip().split(',')[1])

            # shifting the string to right/left
            if shift:
                data = data[1:]
            else:
                data = '0'+data[:]

            # exploded (neglecting the last 10-11 numbers bcoz it's beyond 18th position)
            data = data[:data.rfind('-')].replace('-','')

            # conversion hexa to deci and getting things in pair
            data1 = [int(data[i]+data[i+1], 16) for i in range(0, len(data)-1, 2) if (data[i] != '0' and data[i+1] != '0')]

            # getting max, min and mean value
            max_value = max(data1)
            min_value = min(data1)

            dict_describe['max'].append(max_value)
            dict_describe['min'].append(min_value)
            dict_describe['mean'].append((max_value + min_value) / 2) 

            #creating params like lat, long, date, time
            # lat >> position (4-9) long >> position (13-18) in default string
            
            params['lat'].append(int(data[2:8], 16))
            params['long'].append(int(data[11:], 16))    

    else:
        print('wrong format')

with open('export.py', 'w') as f:
    f.write(json.dumps(dict_describe))

with open('longlat.py', 'w') as f:
    f.write(json.dumps(params))
import pandas as pd
from scipy.io import netcdf
import numpy as np
import numpy.ma as ma
import matplotlib
import matplotlib.pyplot as plt
import netCDF4 as nc
#file1 = open("test data.nc","r")
file1 = 'test data.nc'
dataset = nc.Dataset(file1)

dff = {}
a = b =[]
for i in dataset.variables:
    ditem = dataset[i][:]
    a.append(i)
    b.append(ditem)
    #print(i)
    #print((dataset[i][:]))
df = pd.DataFrame(a,b)
print(df)
#print(df)



"""
file2read = netcdf.NetCDFFile('test data.nc','r')
temp = file2read.variables['u'] # var can be 'Theta', 'S', 'V', 'U' etc..
data = temp[:]*1
print(data)
file2read.close()


"""
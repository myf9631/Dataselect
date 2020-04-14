import netCDF4
from netCDF4 import Dataset
nc_obj=Dataset('ai_challenger_wf2018_trainingset_20150301-20180531.nc')

#查看nc文件有些啥东东
print(nc_obj)
print('---------------------------------------')

#查看nc文件中的变量
# print(nc_obj.variables.keys())
# for i in nc_obj.variables.keys():
#     print(i)
# print('---------------------------------------')

#查看每个变量的信息
# print(nc_obj.variables)
# print(nc_obj.variables['LON'])
# print(nc_obj.variables['PRCP'])
# print('---------------------------------------')

# #查看每个变量的属性
# print(nc_obj.variables['LAT'].ncattrs())
# print(nc_obj.variables['LON'].ncattrs())
# print(nc_obj.variables['PRCP'].ncattrs())
# print(nc_obj.variables['LAT'].units)
# print(nc_obj.variables['LON'].units)
# print(nc_obj.variables['PRCP']._Fillvalue)
# print('---------------------------------------')

# #读取数据值
# lat=(nc_obj.variables['LAT'][:])
# lon=(nc_obj.variables['LON'][:])
# prcp=(nc_obj.variables['PRCP'][:])
# print(lat)
# print(lon)
# print('---------------******-------------------')
# print(prcp)

import numpy as np
import pandas as pd
import os
import sys
import os.path
import datetime,time
#from datetime import timedelta
#from datetime import datetime
import math
from scipy.interpolate import Rbf

lon=[]
lat=[]
for j in range(56,120,1):
  for i in range(56,120,1):
    lon1=105.0+i*0.125
    lat1=50.0-j*0.125
    lon.append(lon1)
    lat.append(lat1)


sta_file='d:\\VBDemo\\stainfo.txt'
data_sta = np.genfromtxt(sta_file,delimiter=",",dtype=None)
sta_list=[]
olat=[]
olon=[]
for line in data_sta:
  sta_list.append(str(line[1]))
  olat.append(str(line[2]))
  olon.append(str(line[3]))
stanum=len(sta_list)
	
#begin_date='2018-02-01 08:00:00'
#jobdate=datetime.strptime(begin_date,"%Y-%m-%d %H:%M:%S")
now=datetime.datetime.now()
jobdate=now+datetime.timedelta(days=-2)
yyyy='%04d' % jobdate.year
yy=yyyy[2:4]
mm='%02d' % jobdate.month
dd='%02d' % jobdate.day
hh='%02d' % jobdate.hour
mi='%02d' % jobdate.minute
if int(hh)>=8 and int(hh)<20:
  jobdate2=yy+mm+dd+'08'
  timeend=int(jobdate2)
  jobdate3=yyyy+'-'+mm+'-'+dd+' '+'08:00:00'
elif int(hh)>=20:
  jobdate2=yy+mm+dd+'20'
  timeend=int(jobdate2)
  jobdate3=yyyy+'-'+mm+'-'+dd+' '+'20:00:00'
  
while int(jobdate2)<=timeend:


  jobdate33=datetime.datetime.strptime(jobdate3,"%Y-%m-%d %H:%M:%S")
  print 'ec jobdate 08 or 20',jobdate33
  jobdate4=jobdate33+datetime.timedelta(hours=-8)
  yyyy4='%04d' % jobdate4.year
  yy4=yyyy4[2:4]
  mm4='%02d' % jobdate4.month
  dd4='%02d' % jobdate4.day
  hh4='%02d' % jobdate4.hour
  jobdate5=yyyy4+mm4+dd4+hh4
  print 'jobdate utc ',jobdate5

  t2_points=[[0 for col in range(17)] for row in range(stanum)]
  u10_points=[[0 for col in range(17)] for row in range(stanum)]
  v10_points=[[0 for col in range(17)] for row in range(stanum)]
  td2_points=[[0 for col in range(17)] for row in range(stanum)]
  r6_points=[[0 for col in range(8)] for row in range(stanum)]
  rh=[[0 for col in range(17)] for row in range(stanum)]  
  es=[[0 for col in range(17)] for row in range(stanum)]
  e=[[0 for col in range(17)] for row in range(stanum)]
  ff=[[0 for col in range(17)] for row in range(stanum)]
  di=[[0 for col in range(17)] for row in range(stanum)]
  
  for val in range(0,17):###### 3hr forecast to 48  ###############
      
    valid=(val)*3

	
    t2=[]
    td2=[]
    u10=[]
    v10=[]
    r6=[]
	
    valid1='%02d' % valid
  
    t2_file='K:\\ecmwf_thin\\2T\\999\\'+jobdate2+'.0'+valid1
    td2_file='K:\\ecmwf_thin\\2D\\999\\'+jobdate2+'.0'+valid1
    u10_file='K:\\ecmwf_thin\\10U\\999\\'+jobdate2+'.0'+valid1
    v10_file='K:\\ecmwf_thin\\10V\\999\\'+jobdate2+'.0'+valid1
    r6_file='K:\\ecmwf_thin\\TP\\r6\\'+jobdate2+'.0'+valid1
    print t2_file
    print td2_file
    print u10_file
    print v10_file
    print r6_file
    
################# t 2m #################################################	
    #print t2_file
    ec_t2 = np.genfromtxt(t2_file,skip_header=6,dtype=None)
    for j in range(56,120,1):
      for i in range(56,120,1):
        t2.append(ec_t2[j][i])
    #print t2,len(t2)

    #olon,olat=np.meshgrid(olon,olat)
    func=Rbf(lon, lat, t2,function='linear')
    t2_new = func(olon, olat)
    #print t2_new,len(t2_new),'t2'
	
    for z in range(0,len(t2_new)):
      t2_points[z][val]=t2_new[z]

    #print 'lon',len(lon),'lat',len(lat)
    #print len(ec_t2)
    #print lon,lat  
##########################################################################

################# td 2m #################################################	
    #print td2_file
    ec_td2 = np.genfromtxt(td2_file,skip_header=6,dtype=None)
    for j in range(56,120,1):
      for i in range(56,120,1):
        td2.append(ec_td2[j][i])
    #print t2,len(t2)

    #olon,olat=np.meshgrid(olon,olat)
    func=Rbf(lon, lat, td2,function='linear')
    td2_new = func(olon, olat)
    #print td2_new,len(td2_new),'td'
	
    for z in range(0,len(td2_new)):
      td2_points[z][val]=td2_new[z]

    #print 'lon',len(lon),'lat',len(lat)
    #print len(ec_t2)
    #print lon,lat
##########################################################################

################# u10m #################################################	
    #print u10_file
    ec_u10 = np.genfromtxt(u10_file,skip_header=6,dtype=None)
    for j in range(56,120,1):
      for i in range(56,120,1):
        u10.append(ec_u10[j][i])
    #print t2,len(t2)

    #olon,olat=np.meshgrid(olon,olat)
    func=Rbf(lon, lat, u10,function='linear')
    u10_new = func(olon, olat)
    #print u10_new,len(u10_new),'u10'
	
    for z in range(0,len(u10_new)):
      u10_points[z][val]=u10_new[z]

    #print 'lon',len(lon),'lat',len(lat)
    #print len(ec_t2)
    #print lon,lat  
##########################################################################

################# v10m #################################################	
    #print v10_file
    ec_v10 = np.genfromtxt(v10_file,skip_header=6,dtype=None)
    for j in range(56,120,1):
      for i in range(56,120,1):
        v10.append(ec_v10[j][i])
    #print t2,len(t2)

    #olon,olat=np.meshgrid(olon,olat)
    func=Rbf(lon, lat, v10,function='linear')
    v10_new = func(olon, olat)
    #print v10_new,len(v10_new),'v10'
	
    for z in range(0,len(v10_new)):
      v10_points[z][val]=v10_new[z]

    #print 'lon',len(lon),'lat',len(lat)
    #print len(ec_t2)
    #print lon,lat  
##########################################################################

################# r6 #################################################	
    if int(valid) % 6 == 0 and int(valid)!=0:
      print 'r6_file',r6_file
      if os.path.exists(r6_file):
        ec_r6 = np.genfromtxt(r6_file,skip_header=6,dtype=None)
        for j in range(56,120,1):
          for i in range(56,120,1):
            r6.append(ec_r6[j][i])        
      #else:
      #  if val==0:	
      #    for j in range(56,120,1):
      #     for i in range(56,120,1):
      #       r6.append(0.0)

      #olon,olat=np.meshgrid(olon,olat)
      #print 'len(r6)',len(r6)
      func=Rbf(lon, lat, r6,function='linear')
      r6_new = func(olon, olat)
      #print r6_new,len(r6_new),'r6'
    
      for z in range(0,len(r6_new)):
        r6_points[z][(int(val/2)-1)]=np.abs(r6_new[z])

      #print 'lon',len(lon),'lat',len(lat)
      #print len(ec_t2)
      #print lon,lat
##########################################################################
	
  #print 'td2_points',td2_points,'len(td2_points)',len(td2_points[0])
  #print 't2_points',t2_points,'len(t2_points)',len(t2_points[0])
  #print 'u10_points',u10_points,'len(u10_points)',len(u10_points[0])
  #print 'v10_points',v10_points,'len(v10_points)',len(v10_points[0])
  #print 'r6_points',r6_points,'len(r6_points)',len(r6_points[0])
  
  for z in range(0,int(stanum)):
    for val in range(1,17):
      es[z][val]=6.11*np.power(10.0,7.5*t2_points[z][val]/(237.7+t2_points[z][val]))
      e[z][val]=6.11*np.power(10.0,7.5*td2_points[z][val]/(237.7+t2_points[z][val]))
      rh[z][val]=(e[z][val]/es[z][val])*100

      ff[z][val]=np.sqrt(np.power(u10_points[z][val],2)+np.power(v10_points[z][val],2))
      if u10_points[z][val]>=0 and v10_points[z][val]>=0:
        di[z][val]=450.0-(np.arctan(np.abs(v10_points[z][val]/u10_points[z][val]))/np.pi*180.0+180)
      elif u10_points[z][val]<0 and v10_points[z][val]>=0:
        di[z][val]=450.0-(360.0-np.arctan(np.abs(v10_points[z][val]/u10_points[z][val]))/np.pi*180.0)
      elif u10_points[z][val]<=0 and v10_points[z][val]<0:
        di[z][val]=90.0-(np.arctan(np.abs(v10_points[z][val]/u10_points[z][val]))/np.pi*180.0)
      elif u10_points[z][val]>0 and v10_points[z][val]<0:
        di[z][val]=450.0-(180-np.arctan(np.abs(v10_points[z][val]/u10_points[z][val]))/np.pi*180.0)		

  
  filepath='E:\met_ec_out\\'
  if not os.path.exists(filepath):
    os.makedirs(filepath)  
  fn=filepath+'ecthin_'+jobdate5+'.txt'
  fw = file(fn,'w')
  ts_0=[]
  ts_50=[]
  tterr_t2=[]
  ttabserr_t2=[]
  tterr_rh2=[]
  ttabserr_rh2=[]
  tterr_wind=[]
  ttabserr_wind=[]
  for i in range(1,17):    
    valid1=(i)*3
    valid_time=jobdate4+datetime.timedelta(hours=valid1)
    yyyy_v='%04d' % valid_time.year
    mm_v='%02d' % valid_time.month
    dd_v='%02d' % valid_time.day
    hh_v='%02d' % valid_time.hour
    valid_time2=yyyy_v+mm_v+dd_v+hh_v
    
    ser_t2 = pd.Series(np.zeros(stanum),index = sta_list)
    ser_t2=ser_t2.replace(0,np.nan)
    ser_rh2 = pd.Series(np.zeros(stanum),index = sta_list)
    ser_rh2=ser_rh2.replace(0,np.nan)
    ser_wind = pd.Series(np.zeros(stanum),index = sta_list)
    ser_wind=ser_wind.replace(0,np.nan)
    
    sur_file='E:\\met_obs_data\\rsurf.ascii.'+valid_time2
    #surdata = open(sur_file,"r")
    
    if not os.path.exists(sur_file):
      tterr_t2.append(np.nan)
      ttabserr_t2.append(np.nan)
      tterr_rh2.append(np.nan)
      ttabserr_rh2.append(np.nan)
      tterr_wind.append(np.nan)
      ttabserr_wind.append(np.nan)
    
    else:  
      err_t2=[]
      abserr_t2=[]
      err_rh2=[]
      abserr_rh2=[]
      err_wind=[]
      abserr_wind=[]
      nnn=0
      
      for sur_line in open(sur_file):
        if sur_line!="":
          sur_line=sur_line.split()
          #print len(sur_line),len(t2_points[z])
          #print sur_file,'z',z
          if int(sur_line[6])==11:
            ser_t2[str(sur_line[1])]=float(sur_line[9])
          if int(sur_line[6])==52:
            ser_rh2[str(sur_line[1])]=float(sur_line[9])
          if int(sur_line[6])==32:
            ser_wind[str(sur_line[1])]=float(sur_line[9])         
            
      for z in range(0,stanum):  
        sta=sta_list[z]
        err_t2.append(ser_t2[sta]-t2_points[z][i]-273.15) 
        abserr_t2.append(np.abs(ser_t2[sta]-273.15-t2_points[z][i]))
        err_rh2.append(ser_rh2[sta]-rh[z][i])
        abserr_rh2.append(np.abs(ser_rh2[sta]-rh[z][i]))
        err_wind.append(ser_wind[sta]-ff[z][i])
        abserr_wind.append(np.abs(ser_wind[sta]-ff[z][i]))

      tterr_t2.append(np.nanmean(err_t2))      
      ttabserr_t2.append(np.nanmean(abserr_t2))
      tterr_rh2.append(np.nanmean(err_rh2))
      ttabserr_rh2.append(np.nanmean(abserr_rh2))
      tterr_wind.append(np.nanmean(err_wind))
      ttabserr_wind.append(np.nanmean(abserr_wind))
    
    if hh_v in ['00','06','12','18']:
      ser_r6 = pd.Series(np.zeros(stanum),index = sta_list)
      ser_r6=ser_r6.replace(0,np.nan)
      r6_file='E:\\met_obs_data\\rnwst.ascii.'+valid_time2+'_acc6'
      if not os.path.exists(sur_file):
        ts_0.append(np.nan)
      else:
        na_0=0
        nb_0=0
        nc_0=0
        nd_0=0
        na_50=0
        nb_50=0
        nc_50=0
        nd_50=0
        for r6_line in open(r6_file):
          if r6_line!="":
            r6_line=r6_line.split()
            ser_r6[str(r6_line[1])]=float(r6_line[9])
          
      for z in range(0,stanum):
        sta=sta_list[z]
        if r6_points[z][(int(i/2)-1)]>=0.1 and ser_r6[sta]>=0.1:
          na_0+=1
        elif r6_points[z][(int(i/2)-1)]>=0.1 and ser_r6[sta]<0.1:
          nb_0+=1
        elif r6_points[z][(int(i/2)-1)]<0.1 and ser_r6[sta]>=0.1:
          nc_0+=1
        elif r6_points[z][(int(i/2)-1)]<0.1 and ser_r6[sta]<0.1:
          nd_0+=1   
        if r6_points[z][(int(i/2)-1)]>=50 and ser_r6[sta]>=50:
          na_50+=1
        elif r6_points[z][(int(i/2)-1)]>=50 and ser_r6[sta]<50:
          nb_50+=1
        elif r6_points[z][(int(i/2)-1)]<50 and ser_r6[sta]>=50:
          nc_50+=1
        elif r6_points[z][(int(i/2)-1)]<50 and ser_r6[sta]<50:
          nd_50+=1
      if (na_0+nb_0+nc_0)!=0:        
        ts_0.append(float(na_0/(na_0+nb_0+nc_0))) 
      else:
        ts_0.append(np.nan)
      if (na_50+nb_50+nc_50)!=0:        
        ts_50.append(float(na_50/(na_50+nb_50+nc_50))) 
      else:
        ts_50.append(np.nan)

  print 'tterr_t2',tterr_t2
  print 'ttabserr_t2',ttabserr_t2
  print 'tterr_rh2',tterr_rh2
  print 'ttabserr_rh2',ttabserr_rh2
  print 'tterr_wind',tterr_wind
  print 'ttabserr_wind',ttabserr_wind
      
  fw.write("err_t2 ")
  for i in range(0,16):
    if i< (15):
      fw.write('%.2f '%(tterr_t2[i]))
    else:
      fw.write('%.2f\n'%(tterr_t2[i]))
  fw.write("abserr_t2 ")
  for i in range(0,16):
    if i< (15):
      fw.write('%.2f '%(ttabserr_t2[i]))
    else:
      fw.write('%.2f\n'%(ttabserr_t2[i]))
  fw.write("err_rh2 ")
  for i in range(0,16):
    if i< (15):
      fw.write('%.2f '%(tterr_rh2[i]))
    else:
      fw.write('%.2f\n'%(tterr_rh2[i]))
  fw.write("abserr_rh2 ")
  for i in range(0,16):
    if i< (15):
      fw.write('%.2f '%(ttabserr_rh2[i]))
    else:
      fw.write('%.2f\n'%(ttabserr_rh2[i]))
  fw.write("err_wind ")
  for i in range(0,16):
    if i< (15):
      fw.write('%.2f '%(tterr_wind[i]))
    else:
      fw.write('%.2f\n'%(tterr_wind[i]))
  fw.write("abserr_wind ")
  for i in range(0,16):
    if i< (15):
      fw.write('%.2f '%(ttabserr_wind[i]))
    else:
      fw.write('%.2f\n'%(ttabserr_wind[i]))
    
  #fw.write(str(err_t2))
  #fw.write(abserr_t2)
  #fw.write(err_rh2)
  #fw.write(abserr_rh2)
  #fw.write(err_wind)
  #fw.write(abserr_wind)
  #fw.write(ts_0)
  #fw.write(ts_50)  

  fw.close
  
  jobdate=jobdate33+datetime.timedelta(hours=12)
  yyyy='%04d' % jobdate.year
  yy=yyyy[2:4]
  mm='%02d' % jobdate.month
  dd='%02d' % jobdate.day
  hh='%02d' % jobdate.hour
  jobdate2=yy+mm+dd+hh
  jobdate3=yyyy+'-'+mm+'-'+dd+' '+hh+':00:00'
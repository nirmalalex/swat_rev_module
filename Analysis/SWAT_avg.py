#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 16:14:25 2021

@author: nma
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
#data = "/home/nma/Downloads/output.csv"
data2 = "/home/nma/hdd/TCR/GroundWatMod/desert_sim1/Analysis/TxtInOut_agrisoil/output.sub"
##dft = pd.read_fwf(data2)
dft_agri = pd.read_fwf(data2,header=8)
data3 = "/home/nma/hdd/TCR/GroundWatMod/desert_sim1/Analysis/TxtInOut_desert/output.sub"
dft_des = pd.read_fwf(data3,header=8)

plt.plot(dft_agri["SWmm"][2000:3000],label="farm soil")
plt.plot(dft_des["SWmm"][2000:3000],label="degraded")
#%%
dft_a = dft_agri.iloc[:,0]
dft_d = dft_des.iloc[:,0]

bb = []
dt = []
for ii in range(len(dft_a)):
    dt += [int(dft_a[ii][20:24])]
    bb += [int(dft_a[ii][6:10])]
    
agri_dft = pd.DataFrame({"sub":bb,"date":dt,"perco":dft_agri['PERCmm'],"swater":dft_agri["SWmm"]})
des_dft = pd.DataFrame({"sub":bb,"date":dt,"perco":dft_des["PERCmm"],"swater":dft_des["SWmm"]})

#%%
import numpy as np

dd = np.arange(0,len(agri_dft),29)

s_ = []
for ii in range(len(dd)):
    if ii <= 29:
        s_ += [np.sum(agri_dft["swater"][dd[ii]:dd[ii+1]])]
    else :
        break

#%%
swater = []
swater_des = []

for ii in range(1,365+1):
    nw_dft = agri_dft[agri_dft["date"]==ii]
    swater += [np.mean(nw_dft['swater'])]
    nw_desdft = des_dft[des_dft["date"]==ii]
    swater_des += [np.mean(nw_desdft['swater'])]

plt.plot(swater,label="agricultural soil")
plt.plot(swater_des,label="dessert soil")
plt.plot(abs(np.array(swater)-np.array(swater_des)),label="difference")
plt.grid()
plt.legend()
#plt.axline((184, 0), (184, 106), linewidth=1, color='y')
#plt.axline((0, 106), (184, 106), linewidth=1, color='y')
plt.annotate('Point of saturation',
            xy=(184, 106), xycoords='data',
            xytext=(30, 30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle,angleA=0,angleB=90,rad=10"))

plt.title("Soil water content")
plt.xlabel("no. of Days")
plt.ylabel("Soil water (mm)")
plt.savefig("/home/nma/fig.png")

#%%

sli = 2
years_sli = np.arange(0,len(swater),sli)
dif = abs(np.array(swater)-np.array(swater_des))
diff_grad = []
for ii in range(len(years_sli)-1):
    diff_grad += [abs(np.mean(np.gradient(dif[years_sli[ii]:years_sli[ii+1]])))]

diff_grad_dft = pd.DataFrame({'grad':diff_grad},index=years_sli[1:])


plt.plot(diff_grad_dft*20,label='')
plt.plot(swater,label="agricultural soil")
plt.plot(swater_des,label="dessert soil")
plt.plot(abs(np.array(swater)-np.array(swater_des)),label="difference")
#plt.annotate('Point of saturation',
#            xy=(184, 106), xycoords='data',
#            xytext=(30, 30), textcoords='offset points',
#            arrowprops=dict(arrowstyle="->",
#                            connectionstyle="angle,angleA=0,angleB=90,rad=10"))
plt.title("Soil water content")
plt.xlabel("no. of Days")
plt.ylabel("Soil water (mm)")
plt.legend()

#%%taking the value

low_gr_ind = diff_grad.index(min(diff_grad))


#%%
data_des = '/media/nma/misc/UBU20/hdd/TCR/GroundWatMod/desert_sim1/Analysis/TxtInOut_desert/output.std'
data_agri = '/media/nma/misc/UBU20/hdd/TCR/GroundWatMod/desert_sim1/Analysis/TxtInOut_agrisoil/output.std'

dft_stdagri = pd.read_fwf(data_des,header=28)[:379]
dft_stddes = pd.read_fwf(data_agri,header=28,engine='python')


#%%
water_inmm = float(input("water_per_day: "))
area = float(input("total_area: "))
#days = input("total_days: ")

water_v = ((water_inmm/1000)*area*1000000)/(24*60*60)

print("water In volume metercube "+str(water_v))

cana_depth = 3
cana_width = 10
c_cons = 1.932
## water_loss = 

length = (water_v*1000000)/(c_cons*np.sqrt(cana_depth)*cana_width)

length_of_canal = length/1000

print("length of canal: "+str(length_of_canal)+" km")


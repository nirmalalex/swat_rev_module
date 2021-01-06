#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:34:20 2021

@author: nma
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from io import StringIO

data2 = "/home/nma/hdd/TCR/GroundWatMod/desert_sim1/Analysis/TxtInOut_agrisoil/output.std"
##dft = pd.read_fwf(data2)
#data2 = "/media/nma/misc/UBU20/hdd/TCR/GroundWatMod/desert_sim1/Analysis/agristdout.txt"
dft_agri = pd.read_csv(data2,header=20,usecols=range(10),sep=r"[ ]{2,}",engine='python')[1:378]
data3 = "/home/nma/hdd/TCR/GroundWatMod/desert_sim1/Analysis/TxtInOut_desert/output.std"
#data3 = "/media/nma/misc/UBU20/hdd/TCR/GroundWatMod/desert_sim1/Analysis/outputdata.txt"

dft_des = pd.read_csv(data3,header=20,sep=r"[ ]{2,}",usecols=range(10),engine='python')[1:378]
#%%
n = 1
ddd = np.arange(1,12*n+1,1)
ind = []

for ii in range(len(ddd)):
    int_i = dft_des['TIME'].index.get_loc(ddd[-1],method ='bfill')
    ind += [dft_des['TIME'][int_i:].index.get_loc(int(ddd[ii]), method ="nearest")]
#%%
agri = np.array(dft_agri["SW"])
des = np.array(dft_des['SW'])
#%%
from scipy.stats import spearmanr
x_val = np.array(agri_dft["swater"])
y_val = np.array(des_dft["swater"])
xc = np.convolve(x_val, np.ones(5)/5,mode='same')
corr_= spearmanr(x_val, y_val)
dif = np.array(np.abs((x_val-y_val)))

final_dft = pd.DataFrame({"date":des_dft["date"],
                          "swater_agr":agri_dft["swater"],
                          "swater_des":des_dft["swater"]})
final_dft.set_index("date",inplace=True)
#final_dft.diff().plot(figsize=(20,10), linewidth=5, fontsize=20)

final_dft.plot.scatter('swater_agr','swater_des')

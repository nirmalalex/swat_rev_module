#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 16:00:27 2020

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
import plotly.figure_factory as FF
#import plotly.express as px
import plotly.graph_objects as go
import time
#import plotly.io as pio
from netCDF4 import Dataset
import plotly.express as px
dft_agrii = agri_dft.sort_values(by='date')
dft_desee = des_dft.sort_values(by='date')


fin_df = pd.concat([dft_agrii,dft_desee],keys=['agri','dese'])
fin_df.reset_index(inplace=True)  
#fig = go.Figure(px.line_3d(dft_agrii, x="sub", y="date", z="perco",line_group="sub"))
#fig.add_trace(data=px.line_3d(dft_desee,x="sub", 
#                           y="date", z="perco",line_group="sub"))

#fig.add_trace(px.line_3d(x=dft_desee["sub"],y=dft_desee["date"],z=dft_desee["perco"],mode="markers+lines",name="Desser-type",groupby=dft_desee["sub"],marker=dict(
#       size=2,
#       color = "red"
#  )))
fig = go.Figure(px.line_3d(fin_df, x="sub", y="date", z="perco",line_group="sub",color="level_0"))
#fig.add_trace(px.line_3d(dft_desee,x="sub",y="date",z="perco"))

#fig = go.Figure(data=[go.Scatter3d(
#    x=dft_agrii["sub"],
#    y=dft_agrii["date"],
#    z=dft_agrii["perco"],
#    mode='lines+markers',
#    marker=dict(
#        size=2,
#        color=dft_agrii["sub"],                # set color to an array/list of desired values
#        colorscale='turbo',   # choose a colorscale
#        opacity=0.8
#    )
#)])
fig.write_html("/home/nma/Desktop/3dswat.html")

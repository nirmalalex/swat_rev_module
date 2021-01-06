#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:29:11 2020

@author: nma
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
#data = "/home/nma/Downloads/output.csv"
data2 = "/home/nma/Documents/output.sub"
##dft = pd.read_fwf(data2)
dftt = pd.read_fwf(data2,header =8)
#%%
dfty = dftt.iloc[:,0]

bb = []
dt = []
for ii in range(len(dfty)):
    dt += [int(dfty[ii][20:24])]
    bb += [int(dfty[ii][6:10])]

dftyd = pd.DataFrame({"sub":bb,"date":dt,"perco":dftt['PERCmm']})
dftyd.to_csv("/home/nma/hdd/TCR/GroundWatMod/woek_dr/out.csv")    
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = "/home/nma/hdd/TCR/GroundWatMod/woek_dr/out.csv"

dft = pd.read_csv(data)

per = []

for ii in range(1,202):
    dfts = dft[dft["sub"]==(ii)][365:731]
    dfftn = dfts[dft["date"] == 1]
    per += [np.mean(dfts)]

perco = pd.DataFrame({"percol":per})
perco.to_csv("/home/nma/Downloads/out2.csv")
#%%
import pandas as pd
import matplotlib.pyplot as plt
data = "/home/nma/hdd/TCR/GroundWatMod/woek_dr/out.csv"

dft = pd.read_csv(data)
import numpy as np
per_date = []
dftn = dft[dft["sub"] == 29]
for ii in range(1,365):
    dfts = dftn[dftn["date"] == ii]["perco"]
    per_date += [np.sum(dfts)]


per_date[0] = 0
per_date[1] = 0

plt.plot(per_date)
plt.title("Daily percolation on a single basin")
plt.ylabel("percolation (mm)")
plt.xlabel("Date")
#plt.grid(True, which='minor')
plt.grid()
plt.savefig("/home/nma/Downloads/fig.png")
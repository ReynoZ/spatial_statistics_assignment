# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:46:21 2022

@author: ZhangXY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

parv = pd.read_table(r'F:\0_Timothy\spatial_statistics_assignment\GSLIBfiles'
                  '\gamv_par5.txt',header=None,usecols=([0]),
                  skiprows=8,comment=('\\'),sep='  ')

num_of_directions = int(parv.iloc[3,0])
num_of_lags = int(parv.iloc[0,0])
num_of_variogram = int(parv.iloc[5+num_of_directions,0])
num_of_skps = num_of_directions*num_of_variogram

row = 0
skp_rows = []
for i in range(num_of_skps):
    skp_rows.append(row)
    row += (num_of_lags+1)

outv_5 = pd.read_csv(r'F:\0_Timothy\spatial_statistics_assignment\GSLIBfiles'
                  '\gamv_out5.txt',header=None,skiprows=skp_rows,
                  usecols=([1,2]),sep='\s+')

outv_10 = pd.read_csv(r'F:\0_Timothy\spatial_statistics_assignment\GSLIBfiles'
                  '\gamv_out10.txt',header=None,skiprows=skp_rows,
                  usecols=([1,2]),sep='\s+')

def set_xy(idx):
    axs[idx].set_xlabel('Distance h/m')
    axs[idx].set_ylabel(r'$\gamma(h)$')
    
fig, axs = plt.subplots(2,1,figsize=(10,8),dpi=200,layout='constrained')
plt.suptitle('Omnidirectional sample variogram for V',fontsize=20)

for i in range(2):
    axs[i].grid(linestyle='--')
    axs[i].set_title(r'Lag $h$ = '+str((i+1)*5)+' m',fontsize=15)
    set_xy(i)
    axs[i].set_xticks(np.arange(0,125,25))
    axs[i].set_ylim(0,110000)

axs[0].plot(outv_5.iloc[1:,0],outv_5.iloc[1:,1],color='b',marker='o')
axs[1].plot(outv_10.iloc[1:,0],outv_10.iloc[1:,1],color='b',marker='o')

fig.savefig('Problem2-1.png')
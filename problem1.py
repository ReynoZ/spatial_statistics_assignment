# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 10:58:13 2022

@author: ZhangXY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

par = pd.read_table(r'F:\0_Timothy\spatial_statistics_assignment\GSLIBfiles'
                  '\gam_par.txt',header=0,usecols=([0,1]),
                  skiprows=9,comment=('\\'),sep='  ')

num_of_directions = int(par.iloc[1,0])
num_of_lags = int(par.iloc[1,1])
num_of_variogram = int(par.iloc[3+num_of_directions,0])
num_of_skps = num_of_directions*num_of_variogram

row = 0
skp_rows = []
for i in range(num_of_skps):
    skp_rows.append(row)
    row += (num_of_lags+1)

out = pd.read_csv(r'F:\0_Timothy\spatial_statistics_assignment\GSLIBfiles'
                  '\gam_out.txt',header=None,skiprows=skp_rows,
                  usecols=([1,2]),sep='\s+')

def set_xy(idx):
    axs[idx].set_xlabel('Distance h/m')
    axs[idx].set_ylabel(r'$\gamma(h)$')
    
fig, axs = plt.subplots(1,2,figsize=(6,3),dpi=200,layout='constrained')
plt.suptitle('Variogram of the 118 Z values at two lag spacings')

for i in range(2):
    axs[i].grid(linestyle='--')
    axs[i].set_title(r'Lag $h$ = '+str((i+1)*2)+' m',fontsize=10)
    set_xy(i)
    axs[i].set_xticks(np.arange(0,22*(i+1),2*(i+1)))
    axs[i].set_ylim(0,80)

axs[0].plot(out.iloc[:num_of_lags,0],out.iloc[:num_of_lags,1],color='b')
axs[1].plot(out.iloc[num_of_lags:,0],out.iloc[num_of_lags:,1],color='b')

fig.savefig('Problem1.png')

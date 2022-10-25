# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:41:48 2022

@author: ZhangXY
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

parv9 = pd.read_table(r'F:\0_Timothy\spatial_statistics_assignment\GSLIBfiles'
                  '\gamv_par.txt',header=None,usecols=([0]),
                  skiprows=8,comment=('\\'),sep='  ')

num_of_directions = int(parv9.iloc[3,0])
num_of_lags = int(parv9.iloc[0,0])+2
num_of_variogram = int(parv9.iloc[5+num_of_directions,0])
num_of_skps = num_of_directions*num_of_variogram

row = 0
skp_rows = []
for i in range(num_of_skps):
    skp_rows.append(row)
    row += (num_of_lags+1)

outv_9 = pd.read_csv(r'F:\0_Timothy\spatial_statistics_assignment\GSLIBfiles'
                  '\gamv_out9.txt',header=None,skiprows=skp_rows,
                  usecols=([1,2]),sep='\s+')

def set_xy(a,b):
    axs[a,b].set_xlabel('Distance h/m')
    axs[a,b].set_ylabel(r'$\gamma(h)$')
    
fig, axs = plt.subplots(5,2,figsize=(8,10),dpi=200,layout='constrained')
plt.suptitle('Nine directional sample variograms',fontsize=20)

name = ['N90°E','N70°E','N50°E','N30°E','N10°E',
        'N10°W','N30°W','N50°W','N70°W','Nan']

count = 0
for i in range(5):
    for j in range(2):
        axs[i,j].grid(linestyle='--')
        set_xy(i,j)
        axs[i,j].set_xticks(np.arange(25,125,25))
        axs[i,j].set_yticks([80000])
        axs[i,j].set_ylim(0,100)
        axs[i,j].set_ylim(0,120000)
        axs[i,j].set_title(name[count],fontsize=12)
        axs[i,j].spines['right'].set_visible(False)
        axs[i,j].spines['top'].set_visible(False)
        k=1+count*num_of_lags
        f=(count+1)*num_of_lags
        axs[i,j].plot(outv_9.iloc[k:f,0],outv_9.iloc[k:f,1],color='C1')
        count+=1

plt.delaxes(axs[4,1])

fig.savefig('Problem2-2.png')
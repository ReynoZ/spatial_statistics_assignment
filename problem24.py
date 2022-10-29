# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:34:34 2022

@author: ZhangXY
"""

import numpy as np
import matplotlib.pyplot as plt
from readout import readout

def set_xy(a,b):
    axs[a,b].set_xlabel('Distance h/m')
    axs[a,b].set_ylabel(r'$\gamma(h)$')

outv_7 = readout('gamv_par710.txt', 'gamv_out7.txt')

new7 = np.array(outv_7).reshape(8,12,2)

fig, axs = plt.subplots(2,2,figsize=(8,5),dpi=200,layout='constrained')
plt.suptitle('Directional sample variograms of V for various'
             ' angular tolerances', fontsize=15)
atol = [10,20,30,40]

count = 0
for i in range(2):
    for j in range(2):
        set_xy(i,j)
        axs[i,j].set_xticks([100])
        axs[i,j].set_yticks([0,60000,120000])
        axs[i,j].set_ylim(0,100)
        axs[i,j].set_ylim(0,120000)
        axs[i,j].spines['right'].set_visible(False)
        axs[i,j].spines['top'].set_visible(False)
        axs[i,j].plot(new7[count,1:,0],new7[count,1:,1],
                       label='N76°E')
        axs[i,j].plot(new7[count+4,1:,0],new7[count+4,1:,1],
                       label='N14°W',ls='--')
        axs[i,j].legend()
        axs[i,j].text(20,20000,'atol='+str(atol[count])+'°')
        count+=1
        
fig.savefig('Problem2-4.png')

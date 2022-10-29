# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:19:52 2022

@author: ZhangXY
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from readout import readout

outv_9 = readout('gamv_par.txt', 'gamv_out9.txt')

new9 = np.array(outv_9).reshape(9,12,2)

ranges = []
for drx in range(9):
    for i in range(11):
        if new9[drx,i,1]<80000<new9[drx,i+1,1]:
            d = 80000 - new9[drx,i,1]
            dy = new9[drx,i+1,1] - new9[drx,i,1]
            dx = new9[drx,i+1,0] - new9[drx,i,0]
            dis = new9[drx,i,0]+(d/dy)*dx
            ranges.append(dis)
            break

ang = np.array([0,20,30,60,80,100,120,140,160])
ang = np.append(ang,ang+180)
rad = ang/180*math.pi
ranges = np.array(ranges)
ranges = np.append(ranges,ranges)

fig = plt.figure(figsize=(5,5),dpi=200)
ax = plt.subplot(111, projection='polar')
ax.stem(rad,ranges)

fig.savefig('Problem2-3.png')

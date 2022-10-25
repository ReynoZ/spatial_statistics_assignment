# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:24:06 2022

@author: ZhangXY
"""

def readout(par,out):
    import pandas as pd
    
    parv = pd.read_table(r'F:\0_Timothy\spatial_statistics_assignment'
                          '\GSLIBfiles\\'+par,header=None,
                          usecols=([0]),skiprows=8,comment=('\\'),sep='  ')

    num_of_directions = int(parv.iloc[3,0])
    num_of_lags = int(parv.iloc[0,0])+2
    num_of_variogram = int(parv.iloc[5+num_of_directions,0])
    num_of_skps = num_of_directions*num_of_variogram

    row = 0
    skp_rows = []
    for i in range(num_of_skps):
        skp_rows.append(row)
        row += (num_of_lags+1)

    outv = pd.read_csv(r'F:\0_Timothy\spatial_statistics_assignment'
                      '\GSLIBfiles\\'+out,header=None,skiprows=skp_rows,
                      usecols=([1,2]),sep='\s+')
    return outv
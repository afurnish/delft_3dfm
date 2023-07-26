#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Read in the tidal data and perform analysis - start with gauge data. 

Created on Tue Jul 25 11:45:48 2023
@author: af
"""

#%% Import in dependecies
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import ttide as tt
from o_functions.start import opsys2; start_path = opsys2()
import glob

#%% Data paths 
tide_gauge_data = start_path + r'modelling_DATA/kent_estuary_project/validation/tidal_validation/1.reformatted'


#%% Functions. 

# This needs to run as a series of just data points where the dt is the timestage and insert 
# stime : float (mpl_datenum) or python datetime
#        The start time of the series, in matplotlib_datenum format (default empty).
tt.t_tide(elevation, dt = 1/12,out_style='pandas', stime = ) 

#%% 
# Tide Gauge Data setup
for file in glob.glob(tide_gauge_data + '/*'):
    df = pd.read_csv(file, parse_dates=['Date'], index_col='Date')
    print(df)
    # Step 2: Filter the DataFrame to include only dates between 1st October 2013 and 1st March 2014
    start_date = '2013-10-01'
    end_date = '2014-11-14'
    filtered_df = df[(df.index >= start_date) & (df.index <= end_date)]
    
    elevation = filtered_df.Height.values
    analysis = tt.t_tide(elevation, dt = 1/96,out_style='pandas', stime = filtered_df.index[0]) 
    plt.plot(elevation)




# UKC3 setup

# PRIMEA setup
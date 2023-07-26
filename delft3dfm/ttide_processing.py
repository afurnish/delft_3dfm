# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:06:01 2023

@author: aafur
"""

#%% Test case
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import ttide as tt


# Define the time range
start_time = datetime.datetime(2023, 6, 1, 0, 0, 0)  # Start time: June 1, 2023, 00:00:00
end_time = start_time + datetime.timedelta(days=1)  # End time: June 2, 2023, 00:00:00

# Generate time stamps at 5-minute intervals
time_range = pd.date_range(start=start_time, end=end_time, freq='5min')

# Generate fake tidal elevations using a sine wave
period = 12  # 12 hours
amplitude = 2  # Amplitude of the tidal signal
phase_shift = 0  # Phase shift of the tidal signal

elevations = amplitude * np.sin(2 * np.pi * (time_range.hour * 60 + time_range.minute) / (period * 60) + phase_shift)

# Create a pandas DataFrame with the elevations and times
data = {'Time': time_range, 'Elevation': elevations}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
#%% Usage of ttide

elevation = np.array(df.Elevation)

time = 1/ (24*12)
name = tt.t_tide(elevation, dt = 1/12,out_style='pandas')
plt.plot(elevation)

"""
RT and HT distributions for the given sessions
"""
# Root path and directory
import sys
import os

ROOT_PATH = "E:/ADS/python/ams/isaccade"
os.chdir(ROOT_PATH)
sys.path.insert(0, os.path.abspath('.'))

import numpy as np
import pandas as pd
from utils.funcs.readMatfiles import *

# Figure for histograms
import matplotlib.pyplot as plt
from utils.plots.pHIST import *

# Required files
# Loading Dataset
ROOT_PATH = "E:/ADS/python/ams/isaccade"
get_data  = "data"
task      = "MG"
recordings = "fef"
analysis   = "population"
subject    = "m1"

path = "/".join([ROOT_PATH,get_data,task,recordings,analysis,subject])
print(path)

fname        = 'nFeF.mat'
fpath = path+'/'+fname
data_dict1 = load_data(fpath)

fname = 'type/Nrn_cell_mf.mat'
fpath = path+'/'+fname
data_dict2 = load_data(fpath)

# Extracting variables from dictionary
# From dataset1
var = 'SPtime'
data = big_Array(data_dict1[var])
print(data.shape)
SPtimeTarget = data[:,0]
SPtimeGo     = data[:,1]
SPtimeMo     = data[:,2]
# From dataset2
stime = np.transpose(data_dict2['time'])
Mf_activity = data_dict2['Mf_activity']

N = Mf_activity.shape[0] # No. of neurons
eventtarget, eventgo, eventmo = [0, 1, 2]    # Events

# Rasters and spike density functions
event = eventmo
spike_timings = SPtimeMo
iRF, oRF = [0, 1]
for neuron_id in range(0,N,1):
    raster = spike_timings[neuron_id]
    Mf    = Mf_activity[neuron_id,event]
    inMf  = Mf[:,iRF]
    outMf = Mf[:,oRF]

    plt.figure()
    plt.plot(raster,np.cumsum(np.ones(raster.shape),axis=0),marker='|',linestyle='none',color=[.8, .8, .8],markersize=1)
    plt.plot(stime,inMf,color='g')
    plt.plot(stime,outMf,color='r')
    plt.plot([0,0],[0,250],color='k')
    plt.xlim(-1250,750)
    plt.ylim(0,225)
    plt.xlabel('Time from go (in ms)')
    plt.ylabel('Activity (sp/s)')
    plt.title('Neuron id:'+str(neuron_id+1))
    plt.show()

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

fname = 'type/Nrn_cell_pos.mat'
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
Activity = data_dict2['Activity']
POS = data_dict2['POS']
RT  = data_dict2['RT']
HT  = data_dict2['HT']

N = Activity.shape[0] # No. of neurons
eventtarget, eventgo, eventmo = [0, 1, 2]    # Events

# Rasters and spike density functions
event         = eventtarget
spike_timings = SPtimeTarget
all_pos       = 8
sub = [4,1,2,3,6,9,8,7]

for neuron_id in range(0,15,1):

    goLoc = POS[:,neuron_id]
    goLoc = goLoc[~np.isnan(goLoc)]
    raster = spike_timings[neuron_id]

    posActivity = Activity[neuron_id,event]
    plt.subplots(3, 3, figsize=(10,8),layout='tight',sharex=True, sharey=True)

    for pos in range(0,all_pos,1):

        sdf  = posActivity[:,pos]
        trials = np.where(goLoc==pos)[0]
        posRaster = raster[trials,:]
        rt  = RT[trials,neuron_id]
        ht  = HT[trials,neuron_id]

        plt.subplot(3,3,sub[pos])
        plt.plot(posRaster,np.cumsum(np.ones(posRaster.shape),axis=0),marker='|',linestyle='none',color=[.8, .8, .8],markersize=1)
        plt.plot(rt, np.cumsum(np.ones(rt.shape), axis=0), marker='o', linestyle='none',color='g', markersize=1.5)
        plt.plot(-ht, np.cumsum(np.ones(ht.shape), axis=0), marker='^', linestyle='none', color='b', markersize=1.5)
        plt.plot(stime,sdf,color='k',linewidth=1)
        plt.fill_between([25, 175], [250, 250], 0, facecolor=[.8, .8, .8], alpha=0.2)
        plt.vlines(0,0,225,colors='k',linestyles='--')
        plt.xlim(-250,1250)
        plt.ylim(0,225)
        plt.xticks(ticks=list(range(-250,1250,250)),labels=list(range(-250,1250,250)))
        plt.xlabel('Time from target (in ms)')
        plt.ylabel('Activity (sp/s)')

    plt.suptitle('Activity at different target locations for neuron '+str(neuron_id+1))

    plt.show()

    figfolder = 'results/posActivity/'
    figname = 'Neuron' + str(neuron_id + 1) + '_Target.jpg'
    #plt.savefig(root_path + figfolder + figname)

    #plt.close()


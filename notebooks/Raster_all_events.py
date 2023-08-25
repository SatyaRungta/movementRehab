"""
RT and HT distributions for the given sessions
"""
import numpy as np
from utils.funcs.readMatfiles import *
import os

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

fname        = 'FeF1.mat'
fpath = path+'/'+fname
data_dict1 = load_data(fpath)

fname = 'type/Nrn_cell_mf.mat'
fpath = path+'/'+fname
data_dict2 = load_data(fpath)

# Extracting variables from dictionary
# From dataset1
SPtimeTarget = data_dict1['SPtimeTarget']
SPtimeGo = data_dict1['SPtimeGo']
SPtimeMo = data_dict1['SPtimeMo']
# From dataset2
stime = np.transpose(data_dict2['time'])
Mf_activity = data_dict2['Mf_activity']

# Raster and spike density functions
N = Mf_activity.shape[0]                                       # No. of neurons
iRF, oRF = [0, 1]                                              # inside RF, outside RF
eventtarget, eventgo, eventmo = [0, 1, 2]                      # Events
Events   = [eventtarget, eventgo, eventmo]
spike_timings = ['SPtimeTarget','SPtimeGo','SPtimeMo']
elabel = ['Target', 'Go cue', 'saccade']
xlim_event = [[-250, 1500],[-1250, 500],[-1500, 250]]

for neuron_id in range(0,10,1):

    fig, axs = plt.subplots(2, 3, figsize=(8,5), sharey=True)
    plt.style.use(styles[7])
    for id, event in enumerate(Events):
        raster = data_dict1[spike_timings[event]][neuron_id]
        Mf    = Mf_activity[neuron_id,event]
        inMf  = Mf[:,iRF]
        outMf = Mf[:,oRF]

        axs[0,id].plot(raster,np.cumsum(np.ones(raster.shape),axis=0),marker='|',linestyle='none',color=[.8, .8, .8],markersize=.25)
        axs[0,id].plot(stime,inMf,color='g')
        axs[0,id].plot(stime,outMf,color='r')
        axs[0,id].plot([0,0],[0,250],color='k')
        axs[0,id].set_xlim(xlim_event[event])
        axs[0,id].set_ylim(0,225)
        axs[0,id].set_xlabel('Time from '+ elabel[event] + ' (in ms)')
        axs[0,id].xaxis.set_tick_params(labelsize=8)
    fig.suptitle('Neuron id:' + str(neuron_id + 1))
    axs[0,0].set_ylabel('Activity (sp/s)')
    axs[1,0].axis('off')
    axs[1,1].axis('off')
    axs[1,2].axis('off')

    figfolder = 'results/Raster_approach/'
    figname   = 'Event_analysis'+str(neuron_id+1)+'.jpg'
    #plt.savefig(root_path + figfolder + figname)

    plt.show()
    plt.close()

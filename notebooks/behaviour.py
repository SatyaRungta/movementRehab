"""
RT and HT distributions for the given sessions
"""
import os
import sys
#SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.dirname(SCRIPT_DIR))

import numpy as np
from utils.funcs.readMatfiles import *

"""

    # Figure for histograms
    import matplotlib.pyplot as plt
    from utils.plots.pHIST import *

    step = 5
    rtbins = list(range(0,500,step))
    htbins = list(range(0,1500,step))


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

    # Required variables
    HT = data_dict1['HT']
    RT = data_dict1['RT']

    # A. For all sessions
    X = np.ravel(HT)
    X = X[~np.isnan(X)]

    Y = np.ravel(RT)
    Y = Y[~np.isnan(Y)]

    # plots
    plt.figure(layout='tight')
    plt.style.use(styles[1])

    plt.subplot(2,2,1)
    plt.hist(X,htbins)
    plt.xlim(0,2000)
    plt.ylim(0,500)
    plt.xlabel('Delay period (ms)')
    plt.ylabel('# No. of trials')

    plt.subplot(2,2,2)
    plt.hist(Y,rtbins)
    plt.xlim(0,475)
    plt.ylim(0,1250)
    plt.xlabel('Reaction time (ms)')
    plt.ylabel('# No. of Trials')

    plt.suptitle('Collective data from M1 for all experimental sessions')
    plt.show()

    figfolder = 'results/'
    figname   = 'Task_and_behaviour.jpg'
    #plt.savefig(root_path+figfolder+figname)

    #plt.close()


    # B.Grouping HT distribution into 3 parts
    grouping = [
                    [0], 
                ]
    [div pdiv] = div_hist(X, grouping)
    div        = step * ceil(div / step)
    div(1, 1)  = 0

    figure;
    for i = 1:size(div, 1)
        bin = [div(i, 1):step: div(i, 2)];
        ht_bin = histc(X, bin);
        bar(bin, ht_bin, 'barwidth', 1);
        hold
        on;
        
    bar(htbins,hti)
    xlim([750 1250])
    P = findobj(gca,'type','patch')
    set(gca,'Fontsize',12,'xtick',[750:50:1250])
    xlabel('Delay time (in ms)')
    ylabel('# Trials')
    xlim([750 1250])
   

"""
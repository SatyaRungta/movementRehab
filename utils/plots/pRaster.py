# Raster with event markers only


# Raster plot for single position

goLoc = POS[:,neuron_id]
goLoc = goLoc[~np.isnan(goLoc)]
raster = spike_timings[neuron_id]

posActivity = Activity[neuron_id,event]
plt.subplots(3, 3, figsize=(10,8),layout='tight',sharex=True, sharey=True)

pos = 0

sdf  = posActivity[:,pos]
trials = np.where(goLoc==pos)[0]
posRaster = raster[trials,:]
rt  = RT[trials,neuron_id]
ht  = HT[trials,neuron_id]

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



# Raster plot for In and out of movement field
    
id = neuron_id+eg

Mf    = Mf_activity[id,event]
inMf, outMf  = Mf[:,iRF], Mf[:,oRF]

# Raster:
raster = spike_timings[id]
n, m = ~np.isnan(inPOS[:,id]),~np.isnan(outPOS[:,id])
itrial, otrial = inPOS[n,id],outPOS[m,id]
iHT, oHT = inHT[:,id], outHT[:,id]
iRT, oRT = inRT[:,id], outRT[:,id]

#itrial, otrial = itrial[~np.isnan(itrial)], otrial[~np.isnan(otrial)]
iHT, oHT = iHT[~np.isnan(iHT)], oHT[~np.isnan(oHT)]
iRT, oRT = iRT[~np.isnan(iRT)], oRT[~np.isnan(oRT)]

itrial, otrial = itrial.astype('int'), otrial.astype('int')
itrial = itrial-1
otrial = otrial-1
iraster, oraster = raster[itrial,:], raster[otrial,:]

ax.plot(iraster, np.cumsum(np.ones(iraster.shape),axis=0)+len(otrial), marker='.', linestyle='none', color=[.8, .8, .8], markersize=.5)
ax.plot(oraster, np.cumsum(np.ones(oraster.shape),axis=0), marker='.', linestyle='none', color=[.8, .8, .8], markersize=.5)
ax.plot(oRT.tolist(),range(1,len(otrial)+1,1), marker='s', linestyle='none', color= 'r', markersize=.3)
ax.plot(iRT.tolist(),list(range(len(oRT),len(iRT)+len(oRT),1)), marker='s', linestyle='none', color='g', markersize=.3)
ax.plot(stime,inMf,color='g')
ax.plot(stime,outMf,color='r')
ax.plot([0,0],[0,250],color='k')
ax.set_xlim(-250,1500)
ax.set_ylim(0,225)
ax.set_title('Neuron id:' + str(id + 1))

# Raster plot for all 8 positions

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

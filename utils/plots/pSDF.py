# Spike desity function

import matplotlib.pylab as plt
import seaborn as sns
sns.set_theme(style="ticks")

dots = sns.load_dataset("dots")

# Define the palette as a list to specify exact values
palette = sns.color_palette("rocket_r")

# Plot the lines on two facets
sns.relplot(
    data=dots,
    x="time", y="firing_rate",
    hue="coherence", size="choice", col="align",
    kind="line", size_order=["T1", "T2"], palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)


# SDF for 
plt.plot(mfTime,inRF,'-g',linewidth=2,label='inRF')
plt.plot(mfTime,outRF,'-r',linewidth=2,label='outRF')
plt.fill_between(epoch[event],[250, 250],0, facecolor=[.8, .8, .8],alpha=0.2)
plt.vlines(0, 0, 250, linestyles='-',colors='k')
plt.vlines(epoch[event], 0, 250, linestyles='-', colors='k',linewidth=.1)
plt.vlines(troc[event], 0, 250, linestyles='--', colors='k')
plt.axis(xlim[event] + [0, 225])
plt.yticks(ticks=[0,50,100,150,200],labels=[])
plt.xticks(ticks=range(xlim[event][0],xlim[event][1],250),labels=[])
plt.title(stages[event]+' stage')
plt.ylabel('Activity (sp/s)')
plt.yticks(ticks=[0,50,100,150,200], labels=[0,50,100,150,200],fontsize=8)
plt.xticks(range(xlim[event][0],xlim[event][1],250),labels=range(xlim[event][0],xlim[event][1],250),fontsize=8)
plt.legend(loc='upper right', fontsize=6)

# Peristimulus hisotogram SDF
plt.plot(mfTime,inRF,'-g',linewidth=2,label='inRF')
plt.plot(mfTime,outRF,'-r',linewidth=2,label='outRF')
plt.fill_between(epoch[event],[250, 250],0, facecolor=[.8, .8, .8],alpha=0.2)
plt.vlines(0, 0, 250, linestyles='-',colors='k')
plt.vlines(epoch[event], 0, 250, linestyles='-', colors='k',linewidth=.1)
plt.vlines(troc[event], 0, 250, linestyles='--', colors='k')
plt.axis(xlim[event] + [0, 225])
plt.yticks(ticks=[0,50,100,150,200],labels=[])
plt.xticks(ticks=range(xlim[event][0],xlim[event][1],250),labels=[])
plt.title(stages[event]+' stage')
plt.ylabel('Activity (sp/s)')
plt.yticks(ticks=[0,50,100,150,200], labels=[0,50,100,150,200],fontsize=8)
plt.xticks(range(xlim[event][0],xlim[event][1],250),labels=range(xlim[event][0],xlim[event][1],250),fontsize=8)
plt.legend(loc='upper right', fontsize=6)

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


# Plotting AUC curves across time

plt.plot(time,roc,'-k',linewidth=1)
plt.fill_between(time.ravel(),roc,0.5,facecolor=[.8, .8, .8])
plt.vlines(0,0,1,linestyles='-',colors='k')
plt.vlines(troc[event], 0, 250, linestyles=':', colors='b')
plt.axis(xlim[event]+[0.25,1])
plt.xlabel('Time from '+xevents[event]+' (in ms)')
plt.yticks(ticks=[.25,.5,.75,1], labels=[])
plt.xticks(range(xlim[event][0],xlim[event][1],250),labels=range(xlim[event][0],xlim[event][1],250),fontsize=8)
plt.ylabel('AUC',fontsize=8)
plt.yticks(ticks=[0,.25, .5, .75, 1], labels=[0,.25, .5, .75, 1],fontsize=8)

    
# ROC analysis between 2 distributions

plt.hist(x= inSDF,bins= range(-20,240,20),color='g',label = 'iRF')
plt.hist(x=outSDF,bins= range(-20,240,20),color='r',alpha = 0.75, label = 'oRF')
plt.xticks(ticks=[0,50,100,150,200,250],labels=[])
plt.yticks(ticks=[0, 15, 30, 45,60], labels=[])
plt.axis([0,250,0,50])
plt.xticks(ticks=[0, 100, 200], labels=[0,100,200],fontsize=4)
plt.yticks(ticks=[0, 15, 30, 45, 60], labels=[0, 15, 30, 45, 60],fontsize=6)
plt.xlabel('Activity (sp/s)',fontsize=6)
plt.ylabel('Counts',fontsize=6)
plt.legend(loc = 'upper right',fontsize=6)



# Plotting 

plt.plot([0,1],[0,1],linestyle='--',color=[.9,.9,.9])
plt.plot(roc_curve[0],roc_curve[1],'-k',linewidth=0.5,label='ROC')
plt.fill_between(roc_curve[0], roc_curve[1], 0, facecolor=[.8, .8, .8])
plt.xticks(ticks=[0,.25,.50,.75,1], labels=[])
plt.yticks(ticks=[0,.25,.50,.75,1], labels=[])
plt.plot([0, 1], [0, 1], linestyle='--', color=[.9, .9, .9])
plt.legend(loc='upper left', fontsize=6)
plt.xticks(ticks=[0,.25,.5,.75,1], labels=[0,'',.50,'',1],fontsize=6)
plt.yticks(ticks=[0,.25,.5,.75,1], labels=[0,'',.50,'',1],fontsize=6)
plt.ylabel('oRF',fontsize=6)
plt.xlabel('iRF',fontsize=6)
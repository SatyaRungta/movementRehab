import matplotlib.pyplot as plt
import seaborn as sns

styles = plt.style.available
print(styles)

def plot_hist(X,xbins):
    for fig_style in styles:
        plt.style.use(fig_style)
        plt.hist(X,xbins)
        plt.xlabel('Delay period')
        plt.ylabel('# counts')
        plt.title('For all sessions')
        plt.xlim(min(1.1*X),max(1.05*X))
        plt.ylim(min(1.1*X),max(1.05*X))
        plt.show()
        
"""
Histogram with 1 group
##############
plt.subplot(2,2,1)
plt.hist(X,htbins)
plt.xlim(0,2000)
plt.ylim(0,500)
plt.xlabel('Delay period (ms)')
plt.ylabel('# No. of trials')

# Histogram divided into different groups
################################

# PSTH
##############################################


"""
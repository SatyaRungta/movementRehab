import h5py as hy
import numpy as np
import pandas as pd

ROOT_PATH = "E:/ADS/python/ams/isaccade"
get_data  = "data"
task      = "MG"
recordings = "fef"
analysis   = "population"
subject    = "m1"

fpath = "/".join([ROOT_PATH,get_data,task,recordings,analysis,subject])
file  = "nFEF.mat"


filename = "/".join([fpath+file])
data = read_matlab(filename)

# For dates
mdates = [''.join(list(map(chr,np.array(list(r.flat))))) for r in data['mdates']]
#print(mdates)

mfiles = [''.join(list(map(chr,np.array(list(r.flat))))) for r in data['mfiles']]
#print(mfiles)

date = [''.join(list(map(chr,np.array(list(r.flat))))) for r in data['mfiles']]
#print(date)

info = pd.DataFrame({'date':date,'mfiles':mfiles,'mdates':mdates})
info.head()
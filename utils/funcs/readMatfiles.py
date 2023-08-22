"""
To Load datasets from matfiles

"""
from mat4py import loadmat
from mat4py import savemat
import scipy.io as sio
import tables as matpy
import h5py

import numpy as np
import pandas as pd
from IPython.display import display
#################################################################

def getTimestamps(file,data,event):
    Event = data[event, :]
    spktime = {}
    for index, r in enumerate(Event):
        spktime[index] = np.array(file[r])[:, :750]
    return spktime

def load_matfile(fpath):
    arrays = {}
    f = h5py.File(fpath)
    for k, v in f.items():
        arrays[k] = v[()]

        # For large Variables
        if k == 'SPtime':
            Events = [0, 1, 2]
            for events in Events:
                arrays[events] = getTimestamps(f,arrays[k],events)

    return arrays

#################################################################

def load_oldmatfile(fname):
    data_variables = loadmat(fname)
    print(f'Loading matfile: {fname}')
    return data_variables

def load_mtables(fname):
    f = matpy.open_file(fname)
    return f

#################################################################

def read_matlab(filename):
    
    def conv(path=''):
        p = path or '/'
        paths[p] = ret = {}
        for k, v in f[p].items():
            if type(v).__name__ == 'Group':
                ret[k] = conv(f'{path}/{k}')  # Nested struct
                continue
            v = v[()]  # It's a Numpy array now
            if v.dtype == 'object':
                # HDF5ObjectReferences are converted into a list of actual pointers
                ret[k] = [r and paths.get(f[r].name, f[r].name) for r in v.flat]
            else:
                # Matrices and other numeric arrays
                ret[k] = v if v.ndim < 2 else v.swapaxes(-1, -2)
        return ret

    paths = {}
    with h5py.File(filename, 'r') as f:
        return conv()

##################################################################
    
def show_info(dictionary):
    data = []
    for k,v in dictionary.items():
                
        if not(k.endswith('__')):
            
            type_name = type(v).__name__
            
            match type_name:
                case "dict":
                    field_names = list(v.keys()), 
                    dimensions  = len(v)
                    
                case "ndarray":
                    field_names = v.dtype,
                    dimensions  = v.shape
                    
                case "list":
                    field_names = 'list',
                    dimensions  = len(v)
                    
                case "tuple":
                    field_names = 'tuple',
                    dimensions  = len(v)
                
                case _ :
                    field_names = list(v.dtype.names) if len(v.dtype)>0 else v.dtype,
                    dimensions  = len(v.dtype)
            
            info = {
                'Variables' : k, 
                'Type'      : type(v).__name__,  
                'Fields'    : field_names[0],
                'Dim'       : dimensions
            }
            data.append(info)
            
    data = pd.DataFrame(data)
                                                                                                      
    return display(data)

##################################################################

def big_Array(Obj):
    data = np.array([Obj['value']],dtype=object)
    
    return data.reshape(Obj['shape'])

def dict2array(obj):
    data = {}
    for k,v in obj.items():
        data[k] = v[:,0].flat
    
    data = pd.DataFrame(data, columns=list(data.keys()))    
    
    return data

##################################################################

def load_data(filename):
    
    data = {}
    
    try:
        
        f = sio.loadmat(filename)
        print(f'Opening mat file v5.0 Path: {filename}')
        
        def read_mat5(f):
            data = {}
            for k,v in f.items():
                # Removing system variables
                if not(k.endswith("__")):
                    # Variables with fields
                    if v.dtype.fields:
                        fields={}
                        for name in v.dtype.names:
                            fields[name] = v[name]
                        data[k] = fields
                    else:
                        data[k] = v
                        
            return data
        
        data = read_mat5(f)
            
    except NotImplementedError:
        
        f = h5py.File(filename, 'r')
        print(f'Opening mat file v7.0 Path: {filename}')
        
        def reshape_object(obj):
            sz = obj.shape
            obj = obj if (1 in sz and np.diff(sz)<0) else obj.T
            
            return obj
        
        def read_object(obj,f):
            data   = {}
            data['value'] = [f[r][()] for r in obj.flat]            
            data['shape'] = obj.shape
                
            return data
        
        def read_dict(f):
            data = {}
            for k, v in f.items():
                if not(k=='#refs#'):
                    if(isinstance(v,h5py.Dataset)):
                        v = v[()]
                        v = reshape_object(v)
                        if v.dtype=='object':
                            data[k] = read_object(v,f) 
                        else:
                            # Matrices and other numeric arrays
                            data[k] = v                 
                    elif(isinstance(v,h5py.Group)):
                        data[k] = read_dict(f[k])
            return data

        data = read_dict(f)
        
    except:
        ValueError(f'Could not read the file path {filename}')
        
    show_info(data)
        
    return data

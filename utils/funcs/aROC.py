import numpy as np
import pandas as pd


def roc_analysis(iRF,oRF):

    iRF = iRF[np.where(iRF>0)[0]]
    oRF = oRF[np.where(oRF>0)[0]]

    thresholds = list(range(0,250,5))
    in_spk=[]
    out_spk=[]
    for thresh in thresholds:
        ispk   = np.where(iRF<=thresh)[0]
        in_spk.append(len(ispk))
        ospk   = np.where(oRF<=thresh)[0]
        out_spk.append(len(ospk))

    in_spk  = [x/len(iRF) for x in in_spk]
    out_spk = [x/len(oRF) for x in out_spk]

    in_spk  = [0]+in_spk+[1]
    out_spk = [0]+out_spk+[1]

    curve = [in_spk,out_spk]

    return curve


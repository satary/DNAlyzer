import matplotlib.pyplot as plt
plt.ioff()
import json
from threading import Lock
lock=Lock() 

import mpld3

import numpy as np
#from prody import *
#from ref_coords import *
#import os
#import glob

def graph(PBD_index):
    with lock:
        fig, ax = plt.subplots()
        t=np.arange(0., 2., 0.1)
        u=t
        ax.plot(t,u)
        mpld3.fig_to_html(fig)

    return mpld3.draw_fig() 

    



'''def saving_file(PDB_index):
    
    This function creates temporary path
    saves there fetched PDB file
    
    if not os.path.isdir('static')
        os.mkdir('static')'''
       


'''def nucleic_test(pdb_file):
    
    This function tests PDB file for
    DNA chains in it.
    
'''




    

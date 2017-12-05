import matplotlib.pyplot as plt
plt.ioff()
import json
from threading import Lock
lock=Lock() 

import mpld3

import numpy as np
from prody import *
from ref_coords import *
import os, glob
import urllib # downloading file



def graph(PBD_index):
    with lock:
        fig, ax = plt.subplots()
        t=np.arange(0., 2., 0.1)
        u=t
        ax.plot(t,u)
        mpld3.fig_to_html(fig)

    return mpld3.draw_fig() 

    


def saving_file(PDB_index):
    '''
    This function creates temporary path
    saves there fetched PDB file
    '''
    url = 'https://files.rcsb.org/download/%s.pdb' % PDB_index
    if not os.path.isdir('DNAlyzer')
        os.mkdir('DNAlyzer')
    else:
        for filename in glob.glob(os.path.join('analyzer', '*.pdb')):
            os.remove('analyzer', filename) # я еще не поняла, что написать в else
    testfile = urllib.URLopener()
    testfile.retrieve(url, str(time.time()) + '.pdb') # это просто сохраняет файл, но не в папку, хз куда


def nucleic_test(pdb_file):
    '''
    This function tests PDB file for
    DNA chains in it.
    '''





    

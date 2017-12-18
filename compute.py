import matplotlib.pyplot as plt
plt.ioff()
import matplotlib
import json
from threading import Lock
lock=Lock() 

import mpld3
from mpld3 import plugins
import numpy as np
#from prody import *
#from ref_coords import *
#import os, glob
#import urllib # downloading file

s = json.load(open("static/bmh_matplotlibrc.json"))
matplotlib.rcParams.update(s)

t=np.arange(0., 2., 0.1)
u=t

#pie_fracs = [20, 30, 40, 10]
#pie_labels = ["A", "B", "C", "D"]

def draw_fig(pdb_index):
    with lock:
        fig, ax = plt.subplots()
        ax.plot(t,u)
        mpld3.fig_to_html(fig)
    print("Draw fig")
    return mpld3.fig_to_html(fig)

    


#def saving_file(PDB_index):
    '''
    This function creates temporary path
    saves there fetched PDB file
    '''
#    url = 'https://files.rcsb.org/download/%s.pdb' % PDB_index
#    if not os.path.isdir('DNAlyzer'):
#        os.mkdir('DNAlyzer')
#    else:
#        for filename in glob.glob(os.path.join('analyzer', '*.pdb')):
#            os.remove('analyzer', filename) # я еще не поняла, что написать в else
#    testfile = urllib.URLopener()
 #   testfile.retrieve(url, str(time.time()) + '.pdb') # это просто сохраняет файл, но не в папку, хз куда


#def nucleic_test(pdb_file):
    '''
    This function tests PDB file for
    DNA chains in it.
    '''





    

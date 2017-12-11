import matplotlib.pyplot as plt
plt.ioff()
import json
from threading import Lock
lock=Lock()
import numpy as np
import os
import urllib.request, uuid, shutil # used in saving_file function



def graph(PBD_index):
    with lock:
        fig, ax = plt.subplots()
        t=np.arange(0., 2., 0.1)
        u=t
        ax.plot(t,u)
        mpld3.fig_to_html(fig)

    return mpld3.draw_fig() 

    
unique_directory_name = str(uuid.uuid4()) # creates unique directory name

def saving_file(PDB_index):
    '''
    This function creates temporary path with unique
    name and saves there fetched PDB file
    '''
    with lock:
        if not os.path.isdir(unique_directory_name): # creates directory with unique name
            os.mkdir(unique_directory_name)
        url = 'https://files.rcsb.org/download/%s.pdb' % PDB_index
        os.chdir(unique_directory_name) # changing directory to new one
        with urllib.request.urlopen(url) as response, open('%s.pdb' % PDB_index, 'wb' ) as out_file:
            shutil.copyfileobj(response, out_file) # download the file from `url` and save it locally under `file_name` (open)

def nucleic_test(PDB_index):
    '''
    This function tests PDB file for
    DNA chains in it.
    '''
    dna = parsePDB('%s.pdb' % PDB_index)
    dna_selection = dna.selec('nucleic')
    if dna_selection == 0:
        return ""
    else: None
    resids = np.unique(dna.getResnums())
    if (resids.size % 2) == 0
        return ""
    else: None
# better use try except


def deleting_directory():
    '''
    This function deletes created directory
    '''
    os.chdir("../")
    shutil.rmtree("/%s" % unique_directory_name)

    

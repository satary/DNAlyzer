import matplotlib.pyplot as plt
import numpy as np

def compute(PDB_index):
    t = np.arange(0., 2., 0.1)
    u = t
    plt.figure()  
    plt.plot(t, u)
    plt.title('So beautiful line')
    
    return plt.show() 

    

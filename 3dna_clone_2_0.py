
# coding: utf-8

# In[34]:


from pylab import * #mathplotlib + numpy
#ion() #turns interactive mode on
from prody import * 
from ref_coords import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

get_ipython().magic('matplotlib notebook')

def plot_coord_system(pos,M,axes):
    '''
    builds diagram of each base reference coord system
    '''
    axes.quiver(pos[0],pos[1],pos[2],M[0,0],M[0,1],M[0,2],color='g',pivot='tail')
    axes.quiver(pos[0],pos[1],pos[2],M[1,0],M[1,1],M[1,2],color='b',pivot='tail')
    axes.quiver(pos[0],pos[1],pos[2],M[2,0],M[2,1],M[2,2],color='r',pivot='tail')

def axisEqual3D(ax):
    '''
    makes equal steps and axis to make 3d diagram
    '''
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:,1] - extents[:,0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize/2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)
        
def get_middle_frame(V1,V2,R1,R2):
    z1 = R1[:,2]
    z2 = R2[:,2]
     
    hinge = np.cross(z1,z2)/np.linalg.norm(np.cross(z1,z2))
    RollTilt = (np.arccos(dot_product(z1,z2)))
    R_hinge=rmat(hinge,-0.5*RollTilt)
    R2p= np.dot(R_hinge,R2)
    R1p= np.dot(rmat(hinge,0.5*RollTilt),R1)
    Rm =(R1p+R2p)/2.0
    Vm =(V1+V2)/2.0
    return Vm, Rm

def dot_product(v,w):
    return v[0]*w[0]+v[1]*w[1]+v[2]*w[2]

def rmat(axis, phi):
    axis=axis/ np.linalg.norm(axis)
    u1=axis[0]
    u2=axis[1]
    u3=axis[2]
    c=np.cos(phi)
    s=np.sin(phi)
    return np.array([[   c+(1-c)*u1*u1, (1-c)*u1*u2-u3*s, (1-c)*u1*u3+u2*s],
                     [(1-c)*u1*u2+u3*s,  (c+(1-c)*u2*u2),(1-c)*u2*u3-u1*s],
                     [(1-c)*u1*u3-u2*s, (1-c)*u2*u3+u1*s,   c+(1-c)*u3*u3]])

def get_params_for_single_step(o1,o2,R1,R2):
    z1=R1[:,2]
    z2=R2[:,2]
    hinge= np.cross(z1,z2)/np.linalg.norm(np.cross(z1,z2))
    RollTilt= (np.arccos(dot_product(z1,z2)))
    R_hinge=rmat(hinge,-0.5*RollTilt)
    R2p= np.dot(R_hinge,R2)
    R1p=np.dot(rmat(hinge,0.5*RollTilt),R1)
    Rm=(R1p+R2p)/2.0
    om=(o1+o2)/2.0
    [shift,slide,rise]=np.dot((o2-o1),Rm)
    twist= np.rad2deg(np.dot(np.cross(R1p[:,1],R2p[:,1]),Rm[:,2]))
    phi=np.dot(np.cross(hinge,Rm[:,1]),Rm[:,2])

    roll=RollTilt*np.cos(phi)
    tilt=RollTilt*np.sin(phi)
    return shift,slide,rise,np.rad2deg(tilt),np.rad2deg(roll),twist


# In[125]:


dna = parsePDB('4c64.pdb').select('nucleic')
ref = {'A': parsePDB('ref_frames/BDNA_A.pdb'),
       'T': parsePDB('ref_frames/BDNA_T.pdb'),
       'G': parsePDB('ref_frames/BDNA_G.pdb'),
       'C': parsePDB('ref_frames/BDNA_C.pdb')}
sel_dic = {'A' :'name N9 C8 N7 C5 C6 N1 C2 N3 C4',
           'T': 'name N1 C2 N3 C4 C5 C6',
           'G': 'name N9 C8 N7 C5 C6 N1 C2 N3 C4',
           'C': 'name N1 C2 N3 C4 C5 C6'}


# In[126]:


#target = dna.select('resnum 2')
#t_name = target.getResnames()[0][-1]
resids = np.unique(dna.getResnums()) 

fig = plt.figure() #makes 3d diagram
ax = fig.add_subplot(111, projection='3d')

vecs=[]
matr=[]



if (resids.size%2) == 0: 
    resids= resids.reshape([2,-1]) 
    resids[1]=resids[1,::-1] 
    resids = resids.T
    
    for indexes in resids:
        targetA = dna.select('resnum %d' % indexes[0]) 
        targetB = dna.select('resnum %d' % indexes[1])
        
        t_nameA = targetA.getResnames()[0][-1]
        t_nameB = targetB.getResnames()[0][-1]
        
        targetA=targetA.select(sel_dic[t_nameA])
        targetB=targetB.select(sel_dic[t_nameB])
        
        fitgroupA=ref[t_nameA].select(sel_dic[t_nameA]).copy()
        fitgroupB=ref[t_nameB].select(sel_dic[t_nameB]).copy()

        
        transformationA= calcTransformation(fitgroupA,targetA,weights=None)

        MrefA= transformationA.getRotation()
        #print np.sum((np.matrix(MrefA).getI()-MrefA.T)**2)
        VrefA= transformationA.getTranslation()
        
        plot_coord_system(VrefA, MrefA,ax)
        
        transformationB= calcTransformation(fitgroupB,targetB,weights=None)
        
        MrefB= transformationB.getRotation()
        #print np.sum((np.matrix(MrefB).getI()-MrefB.T)**2)
        VrefB= transformationB.getTranslation()
        
        MrefB[:,1:]=-MrefB[:,1:]
        plot_coord_system(VrefB, MrefB,ax)
      
        
        Vm, Rm = get_middle_frame(VrefA, VrefB, MrefA, MrefB)
        vecs.append(Vm)
        matr.append(Rm)
        
        
        
        #plot_coord_system(Vm,Rm,ax)
        print Vm
        print Rm
        
else:
    print ""

vecs= np.array(vecs)
vecs1= np.array(vecs1)
        
axisEqual3D(ax)


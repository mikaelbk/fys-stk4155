from matplotlib.pyplot import *
import numpy as np
import scipy.sparse as sp
np.random.seed(12)
import warnings
import machine_learning

warnings.filterwarning	s("ignore") #Comment this to turn on warnings

### define Ising model parameters	
# system size
L=40
# create 10000 random Ising states
states=np.random.choice([-1, 1], size=(int(1e4),L))
def ising_energies(states,L):
	#This function calculates the energies of the states in the nn Ising Hamiltonian
	J=np.zeros((L,L),)
	for i in range(L):
		J[i,(i+1)%L] -= 1.0
	# compute energies
	E = np.einsum("...i,ij,...j->...",states,J,states)
	return E
# calculate Ising energies
energies=ising_energies(states,L)

hist(energies,bins=100)
show()
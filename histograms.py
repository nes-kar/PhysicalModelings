import numpy as np 
from numpy.random import random as rng
import matplotlib.pyplot as plt 


data = rng(100)
plt.hist(data)
plt.show()
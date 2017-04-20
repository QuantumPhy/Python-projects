import numpy as np
import sklearn.metrics as sk_eval
from sklearn import linear_model as lin
from sklearn import tree
from sklearn import naive_bayes  as nb
from sklearn import neighbors
from sklearn.model_selection import train_test_split

def l2_norm(x):
    x_n = np.copy(x)
    for i in range(x[:,0].size):
        n = np.linalg.norm(x[i,:])
        if n>0:
            x_n[i,:] = x[i,:]/n
    return x_n
    
data = np.genfromtxt('person.txt')
train_features, test_features, train_labels, test_labels = train_test_split(data[:,1:], data[:,0], test_size = 0.33, random_state=3)

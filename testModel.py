import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from c3d import *
from classifier import *
from utils.visualization_util import *
import sys;
import numpy as np;
path = "./testFeatures/1_10.npy";
arr =np.load(path);
print(arr.shape);
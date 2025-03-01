import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from glob import glob
from tqdm import tqdm
import cv2

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
#from tensorflow.keras.utils import plot_model

import warnings
warnings.filterwarnings('ignore')

train_path = "Desktop\Edunet\CV_Edunet\TRAIN"
test_path = "Desktop\Edunet\CV_Edunet\TEST"

x_data = []
y_data = []

for category in glob(train_path+'/*'):
    for file in tqdm(glob(category+'/*')):
        img_array=cv2.imread(file)
        img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
        x_data.append(img_array)
        y_data.append(category.split("/")[-1])

data=pd.DataFrame({'image': x_data,'label': y_data})
import pandas as pd
import numpy as np
import os

csv_path = os.path.join(os.getcwd(), 'metadata\\UrbanSound8K.csv')
sampling_rate = 44100
batch_size = 16
classes = 10
init_lr = 1e-3
epochs = 10

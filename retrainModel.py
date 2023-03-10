import os
import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')


from tflite_model_maker import model_spec
from tflite_model_maker import image_classifier
from tflite_model_maker.config import ExportFormat
from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker.image_classifier import DataLoader

image_path = f'./classified_images/'

data = DataLoader.from_folder(image_path)

train_data, rest_data = data.split(0.8)
validation_data, test_data = rest_data.split(0.5)

''' Choose pretrained model to customize. Options using ModelMaker are:

    'efficientnet_lite0',
    'efficientnet_lite1',
    'efficientnet_lite2',
    'efficientnet_lite3',
    'efficientnet_lite4',
    'mobilenet_v2',
    'resnet_50'

''' 

model_spec = 'efficientnet_lite4'
model = image_classifier.create(
  train_data, 
  validation_data=validation_data,
  model_spec=model_spec,
  epochs=20
)

filename = 'customTFModel.tflite'
file_number = 0
while os.path.exists(f'./custom_models/{filename}'):
    filename = filename + "_" + str(file_number)
    file_number += 1

x = model.export(export_dir='./CustomModels', tflite_filename=filename)
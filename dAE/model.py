import keras.backend as K
from keras.layers import Convolution3D, Lambda, MaxPooling3D, Input, BatchNormalization, Dense, Flatten
from keras.models import Model, Sequential
from keras.optimizers import  Adam
from keras.regularizers import WeightRegularizer
from src.metrics import accuracy, precision_0, precision_1, precision_2, recall_0, recall_1, recall_2
import warnings




def dAE(num_channels, input_dimensions):

    # Hyperaparametre values
    L1_reg = 0.000001
    L2_reg = 0.0001
    initializer = 'he_normal'
    regularizer = WeightRegularizer(l1=L1_reg, l2=L2_reg)

    # Compute input shape, receptive field and output shape after softmax activation
    input_shape = (num_channels,) + input_dimensions
    input_layer = Input(shape=input_shape, name='SCAE_input')

    def encoder():
        pass

    def decoder():
        pass

    model = Model(input=input_layer, output=y)

    return model

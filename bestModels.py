from tensorflow import keras
import scipy.io as sio
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.regularizers import l2
import cameraConfig as cameraconfig;
import configuration as cfg
def best_model_outside_sports(weights_path=cfg.classifier_model_weights):
    
    model = Sequential()
    l1 = Dense(512, input_dim=4096, kernel_initializer='glorot_normal',
                    kernel_regularizer=l2(0.001), activation='relu')
    model.add(l1)
    l1.trainable=False;
    model.add(Dropout(0.6))
    l2dense= Dense(32, kernel_initializer='glorot_normal',
                    kernel_regularizer=l2(0.001));
    l2dense.trainable=False;
    model.add(l2dense)
    ##trained till here
    
    model.add(Dense(512, kernel_initializer='glorot_normal',
                    kernel_regularizer=l2(0.001)))
    model.add(Dropout(0.6))
    model.add(Dense(256, kernel_initializer='glorot_normal',
                    kernel_regularizer=l2(0.001)))
    # model.add(Dropout(0.6))
    model.add(Dense(1, kernel_initializer='glorot_normal',
                    kernel_regularizer=l2(0.001), activation='sigmoid'))
    
    # load_weights(model , weights_path)
    # up tiill now the best model
    
    return model
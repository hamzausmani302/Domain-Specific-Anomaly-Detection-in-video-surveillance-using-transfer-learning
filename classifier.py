from tensorflow import keras
import scipy.io as sio
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.regularizers import l2
import cameraConfig as cameraconfig;
import configuration as cfg


def base_model_classifier(weights_path=cfg.classifier_model_weights):
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
    
    # model.add(Dense(256, kernel_initializer='glorot_normal',
    #                 kernel_regularizer=l2(0.001)))
    # model.add(Dropout(0.6))
    # model.add(Dense(256, kernel_initializer='glorot_normal',
    #                 kernel_regularizer=l2(0.001)))
    # model.add(Dropout(0.6))
    model.add(Dense(128 , activation="relu"));

    # model.add(Dense(1, kernel_initializer='glorot_normal',
    #                 kernel_regularizer=l2(0.001), activation='sigmoid'))
    
    model.add(Dense(1,  activation='sigmoid'))
    
    load_weights(model , weights_path)

    
    return model

def classifier_model():
    model = Sequential()
    model.add(Dense(512 , input_dim=4096, kernel_initializer='glorot_normal', kernel_regularizer=l2(0.001), activation='relu'))
    model.add(Dropout(0.6))
    model.add(Dense(32, kernel_initializer='glorot_normal', kernel_regularizer=l2(0.001)))
    model.add(Dropout(0.6))
    model.add(Dense(1, kernel_initializer='glorot_normal', kernel_regularizer=l2(0.001), activation='sigmoid'))
    return model
def build_classifier_model2(t=False):
    model = base_model_classifier();
    weights_path = cfg.classifier_model_weights;
    if(t == True):
        weights_path = cfg.classifier_model_weights_standard
    model = load_weights(model, weights_path)
    return model


def build_classifier_model(t=False):
    model = classifier_model()
    weights_path = cfg.classifier_model_weights;
    if(t == True):
        weights_path = cfg.classifier_model_weights_standard
    model = load_weights(model, weights_path)
    return model

def build_classifier_model1(camera):
    model = classifier_model()
    weights_path = cameraconfig.getCameraModel(camera);
    model = load_weights(model, weights_path)
    return model


def conv_dict(dict2):
    dict = {}
    for i in range(len(dict2)):
        if str(i) in dict2:
            if dict2[str(i)].shape == (0, 0):
                dict[str(i)] = dict2[str(i)]
            else:
                weights = dict2[str(i)][0]
                weights2 = []
                for weight in weights:
                    if weight.shape in [(1, x) for x in range(0, 5000)]:
                        weights2.append(weight[0])
                    else:
                        weights2.append(weight)
                dict[str(i)] = weights2
    return dict


def load_weights(model, weights_file):
    dict2 = sio.loadmat(weights_file)
    dict = conv_dict(dict2)
    i = 0
    for layer in model.layers:
        weights = dict[str(i)]
        layer.set_weights(weights)
        i += 1
    return model

if __name__ == '__main__':
    model = build_classifier_model()
    model.summary()
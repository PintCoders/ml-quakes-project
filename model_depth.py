from model_factory import ModelFactory
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Embedding, Activation, Lambda, Bidirectional

class ModelDepth(ModeFactory):
    def create(self):
        self.model = Sequential()
        model = Sequential()
        model.add(Dense(46,  input_shape=(self.dim,), activation='selu'))
        model.add(Dense(512, activation='sigmoid'))
        model.add(Dense(1, activation='softmax'))
        return model

#import tensorflow as tf
from tensorflow import keras
import numpy as np
model = keras.Sequential([keras.layers.Dense(1,input_shape = [1])])
model.compile(optimizer = "sgd",loss = "mean_squared_error")
x = np.array([1,2,3,4,5],dtype=float)
y = np.array([2,4,6,8,10],dtype=float)
model.fit(x,y,epochs = 100)
prediction = model.predict(np.array([6.0]))
print("The value is = ",prediction)
print("successfull....!")
print("complete....!")

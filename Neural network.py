from tensorflow import keras
import numpy as np
model = keras.Sequential([keras.layers.Dense(2,input_shape =[1])])
model.compile(optimizer = "sgd",loss = "mean_squared_error")
x = np.array([1,2,3,4,5], dtype = float)
y = np.array([[3,3],[6,6],[9,9],[12,12],[15,15]],dtype = float)
model.fit(x,y,epochs = 150)
prediction = model.predict(np.array([[6.0]]))
print("The approximate value is =",prediction)

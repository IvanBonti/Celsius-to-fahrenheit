import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

#importacion de datos
temperature_df = pd.read_csv("Tabla de celsius a Fahrenheit.csv")

#visaulizacion de datos
sns.scatterplot(temperature_df['Celsius'], temperature_df['Fahrenheit'])

#cargando el set de datos
X_train = temperature_df['Celsius']
Y_train = temperature_df['Fahrenheit']

#creacion del modelo
model = tf.keras.Sequential() #usamos un modelo secuencial
model.add(tf.keras.layers.Dense(units=1, input_shape=[1])) #creacion de la capa, una sola neurona debido a la simpleza de la relacion que queremos encontrar

#model.summary()

#funcion de perdida para que la red aprenda, tambien hay optimizadores, declaracion a continuacion
model.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

#Entrenamiento del modelo (epocas)
epochs_hist = model.fit(X_train,Y_train,epochs=100)

#evaluacion del modelo
epochs_hist.history.keys()

#Grafico
plt.plot(epochs_hist.history['loss'])
plt.title('Progreso de perdida durante el entrenamiento del modelo')
plt.xlabel('Epochs')
plt.ylabel('Training loss')
plt.legend('training loss')

#pesos (hace que el modelo aprenda)
model.get_weights()

#Predicciones
Temp_C = 0
Temp_F = model.predict([Temp_C])
print(Temp_F)

#La red predijo 31,944756 Error absoluto: 0.055244 o 0.1726375%
#Otra prediccion
Temp_C = 28
Temp_F = model.predict([Temp_C])
print(Temp_F)

#28*9/5 + 32 = 82.4F el modelo tira 82.





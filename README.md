# Primera-red-neuronal
Red neuronal muy sencilla que trabaja haciendo predicciones entre los grados fahrenheit y celsius, la misma usa regresión lineal y el optimizador adam

Proyecto número 1: Convertir Celsius a Fahrenheit

•	Crearemos una red neuronal simple para el proceso de conversión de grados Fahrenheit a Celsius:

•	La ecuación es la siguiente: T(F) = T(C) x 9/5 + 32
Funcionamiento de la red:

•	El objetivo es predecir el valor de la variable Y sabiendo X, este proceso es la regresión.   
¿Qué son las redes neuronales y cómo aprenden?
Cuando creamos una red neuronal tenemos que tener en cuenta que lo que estamos haciendo es imitar el comportamiento del cerebro humano, algunos datos de curiosidad del cerebero: 

•	Tiene más de 100 mil millones de neuronas que se comunican entre sí a través de señales químicas y eléctricas

•	Estas conexiones nos permiten a nosotros aprender, ver, pensar, generar ideas, etc.

•	Las RNA son modelos de procesamiento de información inspirados en el cerebro humano.
Explicación sencilla de cómo nuestro cerebro se da cuenta de lo que estamos viendo:
Supongamos que vamos caminando por la calle y vemos un gato que pasa por enfrente nuestro: 
Cuando la imagen del gato llega al cerebro, éste tiene como meta  darse cuenta de lo que está viendo y decirnos si es un gato o vió otra cosa. 
Llega la imagen al cerebro, se realizan una serie de cálculos para ver si es realmente o no un gato, es decir, busca encontrar correlación entre las características de un gato o no. 
Luego evalúa que tanto acertó con la predicción que hizo y se genera una pérdida, esta le damos el nombre de función de pérdida. 
Actualización de pesos:
Los pesos son lo que hacen que las redes aprendan por sí solas:
 
Los pesos son actualizados, cuando se reduce la función de pérdida, los pesos se van ajustando, van cambiando y esto hace que la red neuronal aprenda. 

Notas red neuronal que aprende a pasar grados Celsius a fahrenheit:
1.	Pandas: Librería que sirve para interactuar con los datos que vamos a alimentar a la red
2.	seaborn: Sirve para poder graficar los datos y visualizarlos en un gráfico.
3.	Datos en formato csv: Las redes neuronales leen los datos en formato csv, esto es una tabla dividida por comas, cualquier excel se puede transformar.
4.	Optimizador Adam = Es un optimizador que trabaja por descenso del gradiente
5.	función de pérdida: Para un modelo lineal como este caso usamos una función de pérdida por mínimos cuadrados o también podemos decirle “Regresión lineal”
6.	El optimizador adam se le puede pasar como parámetro un número más cercano a 1 y obtendremos mejores predicciones.

Generalización proyecto 1:
Las redes neuronales que tienen dos columnas de valores y se relacionan mediante una fórmula, como por ejemplo el pasaje de grados Celsius a Fahrenheit, o todo ejemplo en el que se aplique el modelo simple de dado un valor de x se aplica una fórmula y se obtiene un y, se realiza con regresión lineal, podemos aplicar una capa densa y con unas cuantas vueltas de entrenamiento la red aprende por sí sola. 
El procedimiento de construcción de la IA es el siguiente:
1.	Crear una tabla dónde están los datos que después queremos predecir en formato .csv (cualquier excel se puede cambiar a esta extensión)
2.	Poner el entorno de spyder en la carpeta dónde esté la tabla y empezar a escribir el codigo

Entrenamiento y predicción con el modelo:
Tenemos que la fórmula de pasaje de celsius a fahrenheit es la siguiente: 
T(F) = T(C) * 9/5 +32
Ejemplo:
0C*9/5 + 32 = 32F



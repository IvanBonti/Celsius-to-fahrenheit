#First neural network 
Simple Neural Network that works by making predictions between Fahrenheit and Celsius degrees, it uses linear regression and the Adam optimizer.

Project number 1: Convert Celsius to Fahrenheit

• We will create a simple neural network for the process of converting Fahrenheit degrees to Celsius:

• The equation is as follows: T(F) = T(C) x 9/5 + 32 Network operation:

• The goal is to predict the value of the Y variable knowing X, this process is regression.
What are neural networks and how do they learn? When we create a neural network, we have to keep in mind that what we are doing is imitating the behavior of the human brain, some curious data about the brain:

• It has more than 100 billion neurons that communicate with each other through chemical and electrical signals

• These connections allow us to learn, see, think, generate ideas, etc.

• ANNs are information processing models inspired by the human brain. Simple explanation of how our brain realizes what we are seeing: Let's say we are walking down the street and we see a cat passing by: When the image of the cat reaches the brain, its goal is to realize what it is seeing and tell us if it's a cat or saw something else. The image reaches the brain, a series of calculations are performed to see if it is really a cat or not, that is, it tries to find a correlation between the characteristics of a cat or not. Then it evaluates how well it guessed with the prediction it made and a loss is generated, we give this the name of loss function. Weight update: The weights are what make the neural networks learn on their own:

The weights are updated when the loss function is reduced, the weights are adjusting, changing, and this makes the neural network learn.

Notes neural network that learns to pass Celsius to Fahrenheit degrees:

Pandas: Library that serves to interact with the data that we are going to feed to the network
seaborn: Serves to be able to graph the data and visualize it on a graph.
Data in csv format: Neural networks read data in csv format, this is a table divided by commas, any excel can be transformed.
Adam Optimizer = It is an optimizer that works by gradient descent
loss function: For a linear model like this case we use a loss function by least squares or we can also call it "Linear Regression"
The Adam optimizer can be passed as a parameter a number closer to 1 and we will obtain better predictions.
Generalization project 1: Neural networks that have two columns of values and are related through a formula, such as the passage of Celsius degrees to Fahrenheit, or any example in which the simple model of given a value of x a formula is applied and a y is obtained, is done with linear regression, we can apply a dense layer and with a few training turns the network learns on its own. The procedure for building AI is as follows:

Create a table where the data that we later want to predict is in .csv format (any excel can be changed to this extension)
Put the spyder environment in the folder where the table is and start writing the code
Training and prediction with the model.
The formula for converting from Celsius to Fahrenheit is: T(F) = T(C) * 9/5 + 32 Example: 0C * 9/5 + 32 = 32F

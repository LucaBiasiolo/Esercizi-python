import tensorflow as tf

mnist_dataset = tf.keras.datasets.mnist #load mnist digits dataset from tensorflow

(x_train, y_train), (x_test, y_test) = mnist_dataset.load_data() #divide dataset in training set and testing set

x_train = x_train / 255.0 #colours are numbers between 0 and 255, so dividing by 255 transforms the image in greyscale
x_test = x_test /255.0

print(x_train[0])

#images are 28x28 pixels
#relu means 'rectified linear unit'
#last layer has dimension 10 because 10 is the number of digits (classes) the neural network needs to predict
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

"""The loss function takes a vector of ground truth values and a vector of logits and returns a scalar loss for each example. 
This loss is equal to the negative log probability of the true class: The loss is zero if the model is sure of the correct class.
This untrained model gives probabilities close to random (1/10 for each class), so the initial loss should be close to -log(1/10) ~= 2.3."""
#in this case "ground truth values" means labels and logits are the predictions
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True) #define loss function

model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy']) #compile the NN using adam optimizer class, loss function and accuracy as metric

model.fit(x_train, y_train, epochs=5) #train the model over 5 epochs. This adjusts the parameters of the model and minimizes the loss
model.save('mnist_digits.keras') #save the model to a file

model.evaluate(x_test,  y_test, verbose=2) #check model performance on a testing set

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
]) #use a model that outputs probabilities instead of logits

#TODO: train another NN using letters instead of digits

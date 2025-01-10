lines = []

#simple implementation of a single Perceptron
class Perceptron:
  def __init__(self, num_inputs=3, weights=[1,1,1]): #the third input is 1 because the third weight is a bias weight
    self.num_inputs = num_inputs
    self.weights = weights

  def weighted_sum(self, inputs):
    weighted_sum = 0
    for i in range(self.num_inputs):
      weighted_sum += self.weights[i]*inputs[i] #calculates the weighted sum = w1*x1+w2*x2 +...
    return weighted_sum

  def activation(self, weighted_sum): #We chose the sign function as activation function for simplicity
    if weighted_sum >= 0:
      return 1
    if weighted_sum < 0:
      return -1

  def training(self, training_set): #this perceptron has to be trained with a training_set of tuples
    foundLine = False
    while not foundLine:
      total_error = 0
      for inputs in training_set:
        prediction = self.activation(self.weighted_sum(inputs)) #take the inputs, calculate the weighted sum and then see if the perceptron activates or not
        actual = training_set[inputs]
        error = actual - prediction
        total_error += abs(error)
        for i in range(self.num_inputs):
          self.weights[i] += error*inputs[i] #update weights using w_i = w_i + error*inputs_i

      slope = -self.weights[0]/self.weights[1]
      intercept = -self.weights[2]/self.weights[1]
      y1 = (slope * 0) + intercept
      y2 = (slope * 50) + intercept
      lines.append([[0,50], [y1, y2]])
      
      if total_error == 0:
        foundLine = True
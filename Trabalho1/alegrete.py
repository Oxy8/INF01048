import numpy as np

def compute_mse(b, w, data):
  return np.sum((w * data[:,0] + b - data[:,1])**2) / len(data)

def step_gradient(b, w, data, alpha):
    X = data[:, 0]
    Y = data[:, 1]
    n = len(data)

    y_pred = w * X + b
    error = y_pred - Y

    b_gradient = np.mean(2 * error)
    w_gradient = np.mean(2 * X * error)

    b = b - alpha * b_gradient
    w = w - alpha * w_gradient

    return [b, w]

def fit(data, b, w, alpha, num_iterations):
  b_history = [b]
  w_history = [w]

  for i in range(num_iterations):
     b, w = step_gradient(b, w, data, alpha)
     b_history.append(b)
     w_history.append(w)

  return [b_history, w_history]

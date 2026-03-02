import numpy as np

def linear_regression(X, y):
    # Add a column of ones to X
    X = np.column_stack((np.ones(len(X)), X))
    
    # Calculate the weights using the normal equation
    weights = np.linalg.inv(X.T @ X) @ X.T @ y
    
    # Return the weights as a numpy array
    return weights

# Example usage
X = np.array([[1], [2], [3]])
y = np.array([1, 2, 3])
weights = linear_regression(X, y)
print(weights)  # Output: [0. 1.]

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9], [100, 200, 300, 400]])

newTdArray = np.delete(twoDArray, 5, 0)

print(newTdArray)

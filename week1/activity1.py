import numpy as np

first_10_positive = np.array(list(range(1, 11)))

print(f"The first 10 postivie array is {first_10_positive}")
print(f"The shape of the array is {first_10_positive.shape}")
print(f"The type of the array is {first_10_positive.dtype}")

# Multiply each element by 2.
# If you don't want to create a new array, can use
# first_10_positive *= 2
# But the variable name is not suitable any more after the value is changed.
# So I don't do it like this.
result = first_10_positive * 2
print(f"The result after multiplying each element by 2 is {result}")


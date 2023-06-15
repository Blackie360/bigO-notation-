import matplotlib.pyplot as plt
import numpy as np

def constant_time(n):
    return 1

def logarithmic_time(n):
    return np.log2(n)

def linear_time(n):
    return n

def quadratic_time(n):
    return n**2

def cubic_time(n):
    return n**3

# Input size range
input_sizes = np.arange(1, 11)

# Calculate the time complexities for each input size
constant_values = [constant_time(n) for n in input_sizes]
logarithmic_values = [logarithmic_time(n) for n in input_sizes]
linear_values = [linear_time(n) for n in input_sizes]
quadratic_values = [quadratic_time(n) for n in input_sizes]
cubic_values = [cubic_time(n) for n in input_sizes]

# Plot the time complexities
plt.plot(input_sizes, constant_values, label='O(1)')
plt.plot(input_sizes, logarithmic_values, label='O(log n)')
plt.plot(input_sizes, linear_values, label='O(n)')
plt.plot(input_sizes, quadratic_values, label='O(n^2)')
plt.plot(input_sizes, cubic_values, label='O(n^3)')

# Set up the plot
plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity')
plt.title('Big O Notation')
plt.legend()

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Define the input size range
n = np.linspace(1, 10, 400)

# Define different Big O complexities
O_1 = np.ones_like(n)
O_log_n = np.log(n)
O_n = n
O_n_log_n = n * np.log(n)
O_n_squared = n**2
O_n_cubed = n**3
O_2_power_n = 2**n

# Create a plot
plt.figure(figsize=(10, 6))

# Plot each Big O complexity
plt.plot(n, O_1, label="$O(1)$")
# plt.plot(n, O_log_n, label="$O(\log n)$")
plt.plot(n, O_n, label="$O(n)$")
# plt.plot(n, O_n_log_n, label="$O(n \log n)$")
plt.plot(n, O_n_squared, label="$O(n^2)$")
plt.plot(n, O_n_cubed, label="$O(n^3)$")
plt.plot(n, O_2_power_n, label="$O(2^n)$")

# Add labels and title
plt.yscale("log")  # Use a logarithmic scale for better visualization
plt.xlabel("Input Size (n)")
plt.ylabel("Operations")
plt.title("Big O Notation Comparison")
plt.legend()
plt.grid(True)
plt.ylim(1, 10**6)  # Limit y-axis for better visualization

# Show the plot
plt.show()

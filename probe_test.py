import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt('probe.out')

# Extract columns
time_steps = data[:, 0]
uX_Tave1 = data[:, 0]  # Corrected index for uX_Tave1
uX_Tave2 = data[:, 1]

# Define the time step intervals
time_interval = 5000

# Calculate the corresponding x-axis values
x_values = np.arange(len(time_steps)) * time_interval

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Plot data in each subplot
ax1.plot(x_values, uX_Tave1, label='uX_Tave1', linestyle='-')
ax1.set_ylabel('a')
ax1.legend()

ax2.plot(x_values, uX_Tave2, label='Fx1', linestyle='-')  # Assuming Fx1 should be in a separate subplot
ax2.set_ylabel('b')
ax2.legend()

# Set common title
plt.suptitle('Probe Data and Residuals over Time Steps (Each Point Represents 5000 Time Steps)')

plt.show()

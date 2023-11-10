import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt('probe.out')

# Extract columns
time_steps = data[:, 0]
uX_Tave1 = data[:, 0]
Fx1 = data[:, 2]
uX_Tave2 = data[:, 5]

# Define the time step intervals
time_interval = 5000

# Calculate the corresponding x-axis values
x_values = np.arange(len(time_steps)) * time_interval

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# Plot data in each subplot
ax1.plot(x_values, uX_Tave1, label='uX_Tave1', linestyle='-', marker='o')
ax1.set_ylabel('uX_Tave1')
ax1.legend()

ax2.plot(x_values, Fx1, label='Fx1', linestyle='-', marker='o')
ax2.set_ylabel('Fx1')
ax2.legend()

ax3.plot(x_values[1:], uX_Tave2[1:], label='uX_Tave2', linestyle='-', marker='o')
ax3.set_xlabel('Time Steps')
ax3.set_ylabel('uX_Tave2')
ax3.legend()

# Set common title
plt.suptitle('Probe Data over Time Steps (Each Point Represents 5000 Time Steps)')

plt.show()

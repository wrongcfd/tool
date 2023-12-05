import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt('probe2.out')

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
fig, ((ax1, ax2), (ax3, ax4), (ax5, _)) = plt.subplots(3, 2, figsize=(12, 16), sharex=True)

# Plot data in each subplot
ax1.plot(x_values, uX_Tave1, label='uX_Tave1', linestyle='-', marker='o')
ax1.set_ylabel('uX_Tave1')
ax1.legend()

# Calculate and plot the residual for uX_Tave1
residual_uX_Tave1 = uX_Tave1[1:] - np.mean(uX_Tave1[1:])
ax2.plot(x_values[1:], residual_uX_Tave1, label='Residual uX_Tave1', linestyle='-', marker='o')
ax2.set_ylabel('Residual uX_Tave1')
ax2.legend()

ax3.plot(x_values, Fx1, label='Fx1', linestyle='-', marker='o')
ax3.set_ylabel('Fx1')
ax3.legend()

# Calculate and plot the residual for uX_Tave2
residual_uX_Tave2 = uX_Tave2[1:] - np.mean(uX_Tave2[1:])
ax4.plot(x_values[1:], residual_uX_Tave2, label='Residual uX_Tave2', linestyle='-', marker='o')
ax4.set_xlabel('Time Steps')
ax4.set_ylabel('Residual uX_Tave2')
ax4.legend()

# Plot original uX_Tave2
ax5.plot(x_values, uX_Tave2, label='uX_Tave2', linestyle='-', marker='o')
ax5.set_xlabel('Time Steps')
ax5.set_ylabel('uX_Tave2')
ax5.legend()

# Set common title
plt.suptitle('Probe Data and Residuals over Time Steps (Each Point Represents 5000 Time Steps)')

plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt('probe.out')

# Extract columns
time_steps = data[:, 0]
uX_Tave1 = data[:, 0]
Ux1 = data[:, 1]
uX_Tave2 = data[:, 3]
Ux2 = data[:, 4]

# Define the time step intervals
time_interval = 1000

# Calculate the corresponding x-axis values
x_values = np.arange(len(time_steps)) * time_interval

# Create subplots
fig, ((ax3, ax6), (ax1, ax5)) = plt.subplots(2, 2, figsize=(12, 16), sharex=True)

# Plot data in each subplot
ax1.plot(x_values, uX_Tave1, label='uX_Tave1', linestyle='-')
ax1.set_ylabel('uX_Tave1')
ax1.legend()

ax3.plot(x_values, Ux1, label='Ux1', linestyle='-')
ax3.set_ylabel('Ux1')
ax3.legend()

# Plot original uX_Tave2
ax5.plot(x_values, uX_Tave2, label='uX_Tave2', linestyle='-')
ax5.set_xlabel('Time Steps')
ax5.set_ylabel('uX_Tave2')
ax5.legend()

# Plot original uX_Tave2
ax6.plot(x_values, Ux2, label='uX_2', linestyle='-')
ax6.set_xlabel('Time Steps')
ax6.set_ylabel('uX_2')
ax6.legend()

# Set common title
plt.suptitle('Probe Data and Residuals over Time Steps (Each Point Represents 5000 Time Steps)')

plt.show()

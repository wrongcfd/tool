import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt('probe.out')

# Extract columns
time_steps = data[:, 0]


uX_Tave1 = data[:,4]



# Define the time step intervals
time_interval = 1000
plt.rc('font', size=14)   
# Calculate the corresponding x-axis values
x_values = np.arange(len(time_steps)) * time_interval

# Create subplots
figsize=(18, 6)


plt.plot(x_values[::10], uX_Tave1[::10], label='uX_Tave1', linestyle='-')
plt.xlabel('time step')
plt.ylabel('U')
# Set common title
plt.suptitle('Probe Data Time Steps (Each Point Represents 10000 Time Steps)')

plt.show()

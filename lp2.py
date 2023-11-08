import numpy as np
import matplotlib.pyplot as plt
import math

# Read DNS data
DNSdata = np.loadtxt('DNS.txt', skiprows=1)
x1 = DNSdata[:, 0]
y1 = DNSdata[:, 1]

# Define the dataset files
dataset_files = [
    ('output_Time_200000.txt', 'd2'),
    ('output_Time_400000.txt', 'd4'),
    ('output_Time_600000.txt', 'd6'),
    ('output_Time_800000.txt', 'd8'),
  #  ('output_Time_1000000.txt', 'd10')  # Add this line
]

# Add parameters
nu = 0.00196923

# Create a figure for the plot
plt.figure(figsize=(8, 6))

# Plot DNS data
plt.scatter(x1, y1, marker='o', color='red', s=25, label='DNS')

# Extract data for DNS calculations (to avoid repeating calculations)
half_length = 81
u_tau_dns = math.sqrt(DNSdata[1, 1] / (0.5) * nu)
y_plus_dns = u_tau_dns * x1 / nu

# Process and plot each dataset
for dataset_file, label in dataset_files:
    data = np.loadtxt(dataset_file, skiprows=1)

    # Extract data for the current dataset
    x = np.arange(0.5, 80, 1)  # grids in Y, N=31
    u_x = data[:half_length, 0]
    u_x_ave = data[1:half_length, 1]  # The column contains Ux_ave data and skip 0

    # Calculate u+ y+ for the current dataset
    u_tau = math.sqrt(u_x_ave[0] / (0.5) * nu)
    u_plus = u_x_ave / u_tau
    y_plus = u_tau * x / nu

    # Plot the data for this dataset
    plt.plot(y_plus, u_plus, label=f'U+ ({label})', linestyle='-')

# Use a logarithmic x-axis
plt.xscale('log')
plt.xlim(1, 130)

plt.xlabel('y+')
plt.ylabel('U+')
plt.legend()

# Save the figure
plt.savefig('result_no10.png')
plt.close()

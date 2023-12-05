import numpy as np
import matplotlib.pyplot as plt
import math

# Read DNS data
DNSdata = np.loadtxt('DNS.txt', skiprows=1)
x1 = DNSdata[:, 0]
y1 = DNSdata[:, 1]

OFdata = np.loadtxt('OF.txt', skiprows=1)
x2 = OFdata[:, 2]
y2 = OFdata[:, 3]

# Define the dataset files
dataset_files = [
 #   ('N30lbm_20mv1output_Time_4000000.txt', 'N30_LBM', 0.000276923,31),
  # ('N30cp_0.5Hv2_output_Time_4000000.txt', 'N30_CP_tau1', 0.000276923,31), 
 #  ('N30cp_tau5_output_Time_4000000.txt', 'N30_CP_tau5', 0.000276923,31), 
 #  ('N30cp_tau0.5_output_Time_3000000.txt', 'N30_CP_tau0.5', 0.000276923,31), 
   ('N30cp_tau0.1_output_Time_4000000.txt', 'N30_CP_tau0.1', 0.000276923,31), 
   ('N30cp_tau0.15_output_Time_4000000.txt', 'N30_CP_tau0.15', 0.000276923,31),
   ('N30cp_tau0.2_output_Time_4000000.txt', 'N30_CP_tau0.2', 0.000276923,31),
 #  ('N30cp_tau0.3_output_Time_4000000.txt', 'N30_CP_tau0.3', 0.000276923,31), 
   #('N30cp_0.8H_output_Time_4000000.txt', 'N30_CP_0.8H', 0.000276923,31), 
]

plt.rc('font', size=16)   
# Create a figure for the plot
plt.figure(figsize=(10, 6))
# Plot DNS data
plt.scatter(x1, y1, marker='o', color='red', s=15, label='DNS')

#plt.plot(x2, y2, color='salmon', linewidth=2, label='OF')
# Define colors and line styles for each dataset
colors = ['blue', 'green', 'purple', 'skyblue','steelblue']
line_styles = ['-', '--', ':', '-.', '-']
# Process and plot each dataset
for i, (dataset_file, label, nu, N) in enumerate(dataset_files):
    data = np.loadtxt(dataset_file, skiprows=1)

    # Extract data for the current dataset
    x = np.arange(0.5, N -1, 1)  # grids in Y
    u_x = data[:N, 0]
    u_x_ave = data[1:N, 3]

    # Calculate u+ y+ for the current dataset
    u_tau = math.sqrt(u_x_ave[0] / (0.5) * nu)
    u_plus = u_x_ave / u_tau
    y_plus = u_tau * x / nu

# Plot the data for this dataset with specified color and line style
    plt.plot(y_plus, u_plus, label=f'U+ ({label})', linestyle=line_styles[i], color=colors[i], linewidth=2)

# Use a logarithmic x-axis
plt.xscale('log')
plt.xlim(0.1, 180)

#print(y_plus[0])
plt.xlabel('y+')
plt.ylabel('U+')
plt.legend()

# Save the figure
#plt.savefig('N30_LBM vs CP tau.png')
plt.show()
plt.close()
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
   # ('aaoutput_Time_1000000.txt', 'N60_v1', 0.00110769,61),  # Include nu_60
    ('N30lbm_20mv1output_Time_4000000.txt', 'N30_LBM', 0.000276923,31),
  #  ('N30cp_0.1Hv2_output_Time_4000000.txt', 'N30_CP_0.1H', 0.000276923,31), 
   ('N40_2mv1output_Time_2000000.txt', 'N40_LBM', 0.000492307692307692,41), 
    ('N60_4mv1output_Time_2000000.txt', 'N60_LBM', 0.00110769,61),
#    ('N40cp_0.1H_output_Time_2000000.txt', 'N40_CP_0.1H', 0.000492307692307692,41), 
#    ('N40cp_0.2H_output_Time_2000000.txt', 'N40_CP_0.2H', 0.000492307692307692,41), 
#    ('N40cp_0.5H_output_Time_2000000.txt', 'N40_CP_0.5H', 0.000492307692307692,41), 
   
]

plt.rc('font', size=16)   
# Create a figure for the plot
plt.figure(figsize=(10, 6))
# Plot DNS data
plt.scatter(x1, y1, marker='o', color='red', s=15, label='DNS')

plt.plot(x2, y2, color='salmon', linewidth=2, label='OF')
# Define colors and line styles for each dataset
colors = ['blue', 'green', 'purple', 'skyblue','steelblue']
line_styles = [':', '--', '-', '-.', '-']
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
plt.savefig('N_varies_LBM.png')
plt.show()
plt.close()
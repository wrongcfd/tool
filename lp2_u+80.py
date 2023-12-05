import numpy as np
import matplotlib.pyplot as plt
import math

# Read DNS data
DNSdata = np.loadtxt('DNS.txt', skiprows=1)
x1 = DNSdata[:, 0]
y1 = DNSdata[:, 1]

# Define the dataset files
dataset_files = [
   # ('aaoutput_Time_1000000.txt', 'N60_v1', 0.00110769,61),  # Include nu_60
   # ('bboutput_Time_1000000.txt', 'N60_v2', 0.00110769,61),  # Include nu_60  v2 is the latest version
  #  ('bboutput_Time_2000000.txt', 'N60_v2_2m', 0.00110769,61), 
  #  ('lbmoutput_Time_1000000.txt', 'N60_lbm', 0.00110769,61),  # Include nu_60
    ('1N80output_Time_2000000.txt', 'N80_2m1', 0.00196923,81),  # Include nu_80
    ('2N80output_Time_2000000.txt', 'N80_2m2', 0.00196923,81),
    ('3N80output_Time_2000000.txt', 'N80_2m3', 0.00196923,81),
    ('4N80output_Time_2000000.txt', 'N80_2m4', 0.00196923,81),
    ('5N80output_Time_2000000.txt', 'N80_2m5', 0.00196923,81)
  #  ('N60output_Time_200000.txt', 'N60_2m', 0.00110769,61),
  
]

plt.rc('font', size=16)  # 
# Create a figure for the plot
plt.figure(figsize=(10, 6))

# Plot DNS data
plt.scatter(x1, y1, marker='o', color='red', s=15, label='DNS')

# Process and plot each dataset
for dataset_file, label, nu, N in dataset_files:
    data = np.loadtxt(dataset_file, skiprows=1)

    # Extract data for the current dataset
    x = np.arange(0.5, N -1, 1)  # grids in Y
    u_x = data[:N, 0]
    u_x_ave = data[1:N, 1]

    # Calculate u+ y+ for the current dataset
    u_tau = math.sqrt(u_x_ave[0] / (0.5) * nu)
    u_plus = u_x_ave / u_tau
    y_plus = u_tau * x / nu

    # Plot the data for this dataset
    plt.plot(y_plus, u_plus, label=f'U+ ({label})', linestyle='-', linewidth=1)

# Use a logarithmic x-axis
plt.xscale('log')
plt.xlim(0.1, 180)

#print(y_plus[0])
plt.xlabel('y+')
plt.ylabel('U+')
plt.legend()

# Save the figure
plt.savefig('N80_convergence vs DNS.png')
#plt.show()
plt.close()
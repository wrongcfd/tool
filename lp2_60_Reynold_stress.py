import numpy as np
import matplotlib.pyplot as plt
import math

# Read DNS data
DNSdata = np.loadtxt('DNSALL.txt', skiprows=1)
x1 = DNSdata[:, 0]
y1 = DNSdata[:, 3]
y2 = DNSdata[:, 4]
y3 = DNSdata[:, 5]
# Define the dataset files
dataset_files = [
   # ('aaoutput_Time_1000000.txt', 'N60_v1', 0.00110769,61),  # Include nu_60
  #  ('N60_2mv1output_Time_2000000.txt', 'N60_2m1', 0.00110769,61),  # Include nu_60
   # ('N60_2mv2output_Time_2000000.txt', 'N60_2m2', 0.00110769,61),
   # ('N60_3mv1output_Time_1800000.txt', 'N60_2m3', 0.00110769,61),
    ('N60_4mv1output_Time_2000000.txt', 'N60_2m4', 0.00110769,61),
  
]

plt.rc('font', size=14)  # 
# Create a figure for the plot
plt.figure(figsize=(10, 6))
# Plot DNS data
plt.scatter(x1, y1, marker='o', color='red', s=15, label='DNS_u')
plt.scatter(x1, y2, marker='o', color='red', s=15, label='DNS_v')
plt.scatter(x1, y3, marker='o', color='red', s=15, label='DNS_w')
# Process and plot each dataset
#for dataset_file, label, nu, N in dataset_files:
for i, (dataset_file, label, nu, N) in enumerate(dataset_files):
    data = np.loadtxt(dataset_file, skiprows=1)
     # Extract data for the current dataset
    x = np.arange(0.5, N-1, 1)  # grids in Y
    ux = data[1:N, 0]

    u_ave = data[1:N, 3]
    v_ave = data[1:N, 4]
    w_ave = data[1:N, 5]

    uu_ave = data[1:N, 6]
    vv_ave = data[1:N, 7]
    ww_ave = data[1:N, 8]

# Calculate u+, y+, and add 0, 0
    u_tau = math.sqrt(u_ave[0] / (0.5) * nu)
    u_plus = u_ave / u_tau
    y_plus = u_tau * x / nu
    # Calculate u', v', and w' components
    u_prime = np.sqrt(uu_ave - u_ave**2)
    v_prime = np.sqrt(vv_ave - v_ave**2)
    w_prime = np.sqrt(ww_ave - w_ave**2)

    # Calculate RMS values
    rms_u_prime = u_prime / u_tau
    rms_v_prime = v_prime / u_tau
    rms_w_prime = w_prime / u_tau

    y = np.concatenate([[0], x/60])
    rms_u_prime = np.concatenate([[0], rms_u_prime])
    rms_v_prime = np.concatenate([[0], rms_v_prime])
    rms_w_prime = np.concatenate([[0], rms_w_prime])

   # Define a color for each dataset
    colors = ['steelblue', 'orange', 'green', 'red']
    current_color = colors[i % len(colors)]

    # Plot the data for this dataset
    plt.plot(y, rms_u_prime, label=f'U_prime+ ({label})', linestyle='-', linewidth=1.5, color=current_color)
    plt.plot(y, rms_v_prime, label=f'V_prime+ ({label})', linestyle='--', linewidth=1.5, color=current_color)
    plt.plot(y, rms_w_prime, label=f'W_prime+ ({label})', linestyle=':', linewidth=1.5, color=current_color)


# Use a logarithmic x-axis
#plt.xscale('log')
#plt.xlim(0.1, 180)

#print(y_plus[0])
plt.xlabel('y')
plt.ylabel('RMS')
plt.legend()

# Save the figure
plt.savefig('RMS_UVW.png')
plt.show()
plt.close()
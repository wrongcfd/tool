import numpy as np
import matplotlib.pyplot as plt
import math

# Read DNS data
DNSdata = np.loadtxt('DNSRXX.txt', skiprows=1)
x1 = DNSdata[:, 0] 
y1 = DNSdata[:, 2] 
y2 = DNSdata[:, 3]
y3 = DNSdata[:, 4]

OFdata = np.loadtxt('OFVEL.txt', skiprows=1) 
OFPdata = np.loadtxt('OF.txt', skiprows=2)
xp = OFPdata[:, 2]
yp = OFPdata[:, 3]

xof=OFdata[:, 0] 
uof=OFdata[:, 1]
vof=OFdata[:, 2]
wof=OFdata[:, 3]
uuof=OFdata[:, 7] 
vvof=OFdata[:, 7] 
wwof=OFdata[:, 7]


#y_b= np.trapz(uuof, xof) / (xof[-1] - xof[0])  
tof=(0.065/15.71)**2
rms_u_of = uuof/tof

# print(f"Bulk Velocity: {y_b}")

# Define the dataset files
dataset_files = [
   # ('aaoutput_Time_1000000.txt', 'N60_v1', 0.00110769,61),  # Include nu_60
    ('N30lbm_20mv1output_Time_4000000.txt', 'N30_LBM', 0.000276923,31),
 #  ('N30cp_0.1Hv2_output_Time_4000000.txt', 'N30_CP_0.1H', 0.000276923,31), 
  # ('N30cp_0.2Hv2_output_Time_4000000.txt', 'N30_CP_0.2H', 0.000276923,31), 
   ('N30cp_0.5Hv2_output_Time_4000000.txt', 'N30_CP_0.5H', 0.000276923,31), 
  # ('N30cp_0.8Hv2_output_Time_4000000.txt', 'N30_CP_0.8H', 0.000276923,31), 
  ('N30cp_tau0.1_output_Time_4000000.txt', 'N30_CP_tau0.1', 0.000276923,31), 
 # ('N30cp_tau0.15_output_Time_4000000.txt', 'N30_CP_tau0.15', 0.000276923,31),
  ('N30cp_tau0.2_output_Time_4000000.txt', 'N30_CP_tau0.2', 0.000276923,31),
  ('N30cp_tau0.2_output_Time_4000000.txt', 'N30_CP_tau10', 0.000276923,31),
    #  ('N40_2mv1output_Time_2000000.txt', 'N40_LBM', 0.000492307692307692,41),
    #  ('N60_4mv1output_Time_2000000.txt', 'N60_LBM', 0.00110769,61),  
]
plt.rc('font', size=14)  # 
# Create a figure for the plot
plt.figure(figsize=(18, 10))
# Plot DNS data
plt.scatter(x1, y1, marker='o', color='red', s=15, label='DNS_Ruu')
plt.scatter(x1, y2, marker='o', color='red', s=15, label='DNS_Rvv')
plt.scatter(x1, y3, marker='o', color='red', s=15, label='DNS_Rww')

plt.plot(xof, rms_u_of, linestyle='-', linewidth=1.5, color='pink', label='OF_Rii')

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
    u_xave=data[0:N, 6]
    x2 = np.concatenate([[0], x])
    u_b2=np.trapz(u_xave, x2) / (x2[-1] - x2[0])
# Calculate u+, y+, and add 0, 0
    u_tau = math.sqrt(u_ave[0] / (0.5) * nu)
    u_plus = u_ave / u_tau
    y_plus = u_tau * x / nu
    # Calculate u', v', and w' components
    u_prime = uu_ave - u_ave**2
    v_prime = vv_ave - v_ave**2
    w_prime = ww_ave - w_ave**2

    du=1/(N-1)/0.001 *18.2839
    u_b=1

    rms_u_prime = u_prime /(u_b**2)*(du**2) 
    rms_v_prime = v_prime /(u_b**2)*(du**2)
    rms_w_prime = w_prime /(u_b**2)*(du**2)


    y = np.concatenate([[0], x/(N-1)])
    rms_u_prime = np.concatenate([[0], rms_u_prime])
    rms_v_prime = np.concatenate([[0], rms_v_prime])
    rms_w_prime = np.concatenate([[0], rms_w_prime])

   # Define a color for each dataset
    colors = ['blue', 'green', 'purple', 'skyblue','steelblue']
    current_color = colors[i % len(colors)]

    # Plot the data for this dataset
    plt.plot(y, rms_u_prime, label=f'Ruu ({label})', linestyle='-', linewidth=1.5, color=current_color)
    plt.plot(y, rms_v_prime, label=f'Rvv ({label})', linestyle='--', linewidth=1.5,color=current_color)
    plt.plot(y, rms_w_prime, label=f'Rww ({label})', linestyle=':', linewidth=1.5, color=current_color)


# Use a logarithmic x-axis
#plt.xscale('log')
#plt.xlim(0.1, 180)

#print(y_plus[0])
plt.xlabel('y/H')
plt.ylabel('R')
plt.legend()

# Save the figure
#plt.savefig('N30_R_tau.png')
plt.show()
plt.close()
import numpy as np
import matplotlib.pyplot as plt
import math

# Read DNS data
DNSdata = np.loadtxt('DNSVEL.txt', skiprows=1)
x1 = DNSdata[:, 0]
y1 = DNSdata[:, 1]

OFdata = np.loadtxt('OFVEL.txt', skiprows=1)
xof = OFdata[:, 0]
yof = OFdata[:, 1]

y_b= y1/np.trapz(y1, x1) / (x1[-1] - x1[0])     #x1[0] This refers to the first (initial) y-value in the array y_values. x1[0]
#yofb= yof/np.trapz(yof, xof) / (xof[-1] - xof[0])
yofb=yof/0.065

print(f"DNSBulk Velocity: {np.trapz(y1, x1) / (x1[-1] - x1[0]) }")
print(f"Bulk Velocity: {np.trapz(yof, xof)}")
# Define the dataset files
dataset_files = [
   # ('aaoutput_Time_1000000.txt', 'N60_v1', 0.00110769,61),  # Include nu_60
   # ('bboutput_Time_1000000.txt', 'N60_v2', 0.00110769,61),  # Include nu_60  v2 is the latest version
  #  ('bboutput_Time_2000000.txt', 'N60_v2_2m', 0.00110769,61), 
  #  ('N60_8mv1output_Time_8000000.txt', 'N60_LBM', 0.00110769,61),  # Include nu_60
    ('N30lbm_20mv1output_Time_4000000.txt', 'N30_LBM', 0.000276923,31),
#     ('N30cp_0.1Hv2_output_Time_4000000.txt', 'N30_CP_0.1H', 0.000276923,31), 
#    ('N30cp_0.2Hv2_output_Time_4000000.txt', 'N30_CP_0.2H', 0.000276923,31), 
   ('N30cp_0.5Hv2_output_Time_4000000.txt', 'N30_CP_0.5H', 0.000276923,31), 
    ('N30cp_tau0.1_output_Time_4000000.txt', 'N30_CP_tau0.1', 0.000276923,31), 
   ('N30cp_tau0.15_output_Time_4000000.txt', 'N30_CP_tau0.15', 0.000276923,31),
   ('N30cp_tau0.2_output_Time_4000000.txt', 'N30_CP_tau0.2', 0.000276923,31),

]


plt.rc('font', size=16)  # 
# Create a figure for the plot
plt.figure(figsize=(10, 6))

# Plot DNS data
plt.scatter(x1, y_b, marker='o', color='red', s=15, label='DNS')

plt.plot(xof, yofb, color='salmon', linewidth=2, label='OF')

colors = ['brown', 'green', 'purple', 'skyblue','steelblue']
line_styles = ['-', '--', ':', '-.', '-']
# Process and plot each dataset
for i, (dataset_file, label, nu, N) in enumerate(dataset_files):
    data = np.loadtxt(dataset_file, skiprows=1)

    # Extract data for the current dataset
    x = np.arange(0.5, N-1 , 1)  # grids in Y
    u_x = data[:N, 0]
    u_x_ave = data[1:N, 3]
    u_xave=data[0:N, 3]
    x2 = np.concatenate([[0], x])
    #u_b=u_x_ave*0.03/0.001/result /2/30
    u_b= np.trapz(u_xave, x2) / (x2[-1] - x2[0])

    u_b=u_x_ave/u_b
    # Calculate u+ y+ for the current dataset
    u_tau = math.sqrt(u_x_ave[0] / (0.5) * nu)
    u_plus = u_x_ave / u_tau
    y_plus = u_tau * x / nu
    y=x / (N-1)
    y = np.concatenate([[0], y])
    u_b = np.concatenate([[0], u_b])

    # Plot the data for this dataset with specified color and line style
    plt.plot(y, u_b, label=f'U ({label})', linestyle=line_styles[i], color=colors[i], linewidth=2)
    #plt.plot(y, u_plus, label=f'U+ ({label})', linestyle=line_styles[i], color=colors[i], linewidth=2)

# Use a logarithmic x-axis
#plt.xscale('log')
#plt.xlim(0.1, 180)

#print(y_plus[0])
plt.xlabel('y/H')
plt.ylabel('U/Ub')
plt.legend()
#plt.grid()
# Save the figure
#plt.savefig('N30_Ub.png')
plt.show()
plt.close()
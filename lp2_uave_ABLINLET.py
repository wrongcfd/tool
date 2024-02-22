import numpy as np
import matplotlib.pyplot as plt
import math
def read_N_and_H_from_filename(filename):
    N = None
    cy = None
    dt= None
    for part in filename.split('_'):
        for i, char in enumerate(part):
            if char == 'N' and part[i+1:].isdigit():
                N = int(part[i+1:])
            if char == 'H' and part[i+1:].isdigit():
                cy = int(part[i+1:])
            if char == 't' and i < len(part) - 1 and part[i+1:].replace('.', '').isdigit():
                dt = float(part[i+1:])
    return N, cy,dt

E1999data = np.loadtxt('exp3d_1999_version2.txt')
Edata = np.loadtxt('exp3d.txt', delimiter=',')
data = np.loadtxt('U2016.txt', delimiter=',')
dataset_files = [   
        #   ('3DhillN10_H15_Z15_dt0.01_sigma0.1_Time_100000.txt', '1m'),
        #   ('3DhillN10_H15_Z15_dt0.01_sigma0.1_Time_200000.txt', '1m'),
        #  ('3DhillN10_H15_Z15_dt0.01_sigma0.25_Time_100000.txt', '1m'),
        #  ('3DhillN20_H15_Z15_dt0.001_sigma0.25_Time_400000.txt', '1m'),
        #  ('3DhillN10_H15_Z15_dt0.01_sigma0.25_abl10_re10500_Time_200000.txt', '1m'),
         #  ('3DhillN10_H15_Z15_dt0.005_re12000_smag0.1_Time_200000.txt', '1m'),
            ('3DhillN10_H15_Z15_dt0.005_re12000_Time_200000.txt', '1m'),
        #     ('ABLN10_H15_Z15_dt0.005_re12000_Time_200000.txt', '1m'),

           ('3DhillN20_H15_Z15_dt0.001_re12000_Time_200000.txt', '1m'),
        #    ('ABLN20_H15_Z15_dt0.001_re12000_Time_200000.txt', '1m'),
        
]
x1 = Edata[:, 0]+7; y1 = Edata[:, 1] 
x2 = E1999data[:, 0]+7; y2 = E1999data[:, 1] 
x_data = data[1:, 0] +0.75
y_data = data[1:, 1]  

plt.rc('font', size=16)   
fig = plt.gcf()
# Adjust the position of the subplot
fig.subplots_adjust(left=0.1, right=0.7, top=0.7, bottom=0.3)
# plt.scatter(x1, y1, marker='o', s=50, c='none',edgecolors='r',label='exp_u')
plt.scatter(x2, y2, marker='o', c='none',edgecolors='r', s=50, label='exp_u')


abl=4      # sets abl number 
plt.scatter(np.tile(x_data, abl) + np.repeat(np.arange(0, abl) * 1.25, len(x_data)), 
            np.tile(y_data, abl), marker='*', color='blue', label='Original Data')

# Function parameters
amplitude_xy = 1
frequency_xy = 0.25
length_xy = 2.5

# Generate XS values
XS = np.linspace(4.5, 9.5, 1000)

# Calculate YS values using the given function
sine_hill_YS = amplitude_xy * np.cos(2 * np.pi * frequency_xy * ((XS - 7) / length_xy)) ** 2

# Plot the function
plt.plot(XS, sine_hill_YS)


# Process and plot each dataset
for i, (dataset_file, label) in enumerate(dataset_files):
    N, cy, dt = read_N_and_H_from_filename(dataset_file)
    
    #print(f"Dataset {i + 1}: N = {N}")  # Print the value of N
    data = np.loadtxt(dataset_file, skiprows=1)
    y = np.arange(0, cy, 1/N)
    D = -0.75
    S = 1.25
    Space=23.75
    # Plot for each j value
    print(f"Dataset {i + 1}: N = {N}, cy = {cy}, dt = {dt}")
    du=N*dt
    for j in range(12):
        ux_ave = data[0:(N*cy), int((j * S+Space) * N)-1] /du  #+ 4.5-S*4
        zero_mask = ux_ave != 0  # Mask where ux_ave is not zero
        if zero_mask.any():  # Check if there are non-zero values
            # if i == 0:  # For the first dataset, use a solid line
            #     #plt.scatter(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='-', linewidth=2,color='steelblue')
            #     plt.plot(ux_ave[zero_mask] + S * (j - 0) - D, y[zero_mask], linewidth=2, color='steelblue')
            # elif i == 1:  # For the second dataset, use a dashed line
            #     plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='--', linewidth=2,color='steelblue')
            # elif i == 2:  # For the second dataset, use a dashed line
            #     # plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='-', linewidth=2,color='purple')
            #     plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle=':', linewidth=2,color='steelblue')
            # elif i == 3:  # For the second dataset, use a dashed line
            #     plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='--', linewidth=2,color='purple')

            zero_mask_inv = ~zero_mask
            plt.plot(np.full_like(y[zero_mask_inv], S * (j - 0)-D ), y[zero_mask_inv], color='black', linestyle='-', linewidth=8)


plt.xticks(np.arange(0.75, 20.75, 1.25))
plt.xlim(0, 14.5)
plt.ylim(0,4.2)
plt.xlabel('X/D+u/$U_{\infty}$')
plt.ylabel('Y')
# Get only the handles and labels for solid and dashed lines

# Add legend
#plt.legend()
#plt.legend(['exp','1m',  'hill','1.5m'])
# Save the figure
#plt.savefig('N30_LBM vs CP tau.png')
# Maximize the Tkinter window on the screen
plt.get_current_fig_manager().window.state('zoomed')
plt.show()
plt.close()

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


Edata = np.loadtxt('exp3d.txt', delimiter=',')
data = np.array([
    [0.42626072389834374, 0.03276131045241826],
    [0.5559797902120167, 0.1638065522620904],
    [0.6031931073161294, 0.23868954758190286],
    [0.6339376024020553, 0.3229329173166926],
    [0.6741967637889188, 0.4680187207488298],
    [0.6956029261578627, 0.6037441497659906],
    [0.7455090040336307, 0.8939157566302653],
    [0.7695050659169225, 1.1794071762870515],
    [0.7838762530093042, 1.3338533541341655],
    [0.7864367635929927, 1.4648985959438376],
    [0.8418973493633624, 2.2932917316692665],
    [0.8686743388102871, 2.850234009360374]
])
dataset_files = [   
        #  ('3DhillN10_H15_Z15_dt0.01_sigma0.1_Time_100000.txt', '1m'),
        #  ('3DhillN10_H15_Z15_dt0.01_sigma0.1_Time_200000.txt', '1m'),
        #  ('3DhillN10_H15_Z15_dt0.01_sigma0.25_Time_100000.txt', '1m'),
         ('3DhillN20_H15_Z15_dt0.001_sigma0.25_Time_400000.txt', '1m'),
         ('3DhillN20_H15_Z15_dt0.001_sigma0.1_Time_400000.txt', '1m'),
        
]
x1 = Edata[:, 0]+7; y1 = Edata[:, 1] 
x_data = data[1:, 0] +0.75
y_data = data[1:, 1]  

plt.rc('font', size=16)   
fig = plt.gcf()
# Adjust the position of the subplot
fig.subplots_adjust(left=0.1, right=0.7, top=0.7, bottom=0.3)
plt.scatter(x1, y1, marker='o', color='red', s=50, label='exp_u')
abl=12# sets abl number 
plt.scatter(np.tile(x_data, abl) + np.repeat(np.arange(0, abl) * 1.25, len(x_data)), 
            np.tile(y_data, abl), marker='*', color='blue', label='Original Data')

# Process and plot each dataset
for i, (dataset_file, label) in enumerate(dataset_files):
    N, cy, dt = read_N_and_H_from_filename(dataset_file)
    
    #print(f"Dataset {i + 1}: N = {N}")  # Print the value of N
    data = np.loadtxt(dataset_file, skiprows=1)
    y = np.arange(0, cy, 1/N)
    D = -0.75
    S = 1.25
    # Plot for each j value
    print(f"Dataset {i + 1}: N = {N}, cy = {cy}, dt = {dt}")
    du=N*dt
    for j in range(12):
        ux_ave = data[0:(N*cy), int((j * S+0.75+23) * N)-1] /du  #+ 4.5-S*4
        zero_mask = ux_ave != 0  # Mask where ux_ave is not zero
        if zero_mask.any():  # Check if there are non-zero values
            if i == 0:  # For the first dataset, use a solid line
                #plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask], label=f'Ux_ave_{j} ({label})', linewidth=2)
                plt.plot(ux_ave[zero_mask] + S * (j - 0) - D, y[zero_mask], linewidth=2, color='steelblue')
            elif i == 1:  # For the second dataset, use a dashed line
                plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='--', linewidth=2,color='steelblue')
            elif i == 2:  # For the second dataset, use a dashed line
                # plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='-', linewidth=2,color='purple')
                plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle=':', linewidth=2,color='steelblue')
            elif i == 3:  # For the second dataset, use a dashed line
                plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='--', linewidth=2,color='purple')

            zero_mask_inv = ~zero_mask
            plt.plot(np.full_like(y[zero_mask_inv], S * (j - 0)-D ), y[zero_mask_inv], color='black', linestyle='-', linewidth=8)


plt.xticks(np.arange(0.75, 20.75, 1.25))
plt.xlim(0, 16)
plt.ylim(0,10)
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
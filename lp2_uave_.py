import numpy as np
import matplotlib.pyplot as plt
import math
# Define the dataset files
Edata = np.loadtxt('EXP.txt', delimiter=',')
Edata2 = np.loadtxt('EXP2.txt', delimiter=',')
dataset_files = [
    # ('hillN30_smag0.1_full_Time_1000000.txt', 'uD', 0.000276923,181),
    #  ('hillN30_smag0.2_full_Time_1000000.txt', '1m', 0.000276923,181),
    #  ('hillN30_smag0.2_full_Time_2000000.txt', '1m', 0.000276923,181),
    #  ('hillN30_smag0.14_full_Time_1000000.txt', '1m', 0.000276923,181),
    # ('hillN30_smag0.14_full_Time_1000000.txt', '1m', 0.0001,181),
    #    ('hillN30_smag0.14_full_Time_2000000.txt', '1m', 0.0001,181),
    # #   ('hillN30_smag0.05_full_Time_1000000.txt', '1m', 0.0001,181),
    #    ('hillN30_smag0.05_full_Time_2000000.txt', '1m', 0.0001,181),

   #('hillN20_smag0.14_full_dt0.0001_Time_1000000.txt', '1m', 0.0001,121),
   #('hillN30_smag0.14_half_Time_1000000.txt', '1m', 0.0001,181),
  #  ('hillN30_smag0.14_full_Time_1000000.txt', '1m', 0.0001,181),
    #('hillN40_smag0.1_half_1000000.txt', '1m', 0.0001,241),

    #  ('hillN30_smag0.14_full_dt0.001_Time_500000.txt', '1m', 0.001,181),
    #  ('hillN30_smag0.14_full_dt0.001_Time_1000000.txt', '1m', 0.001,181),
    #  ('hillN20_smag0.14_full_dt0.0001_Time_1000000.txt', '1m', 0.0001,121),
    #  ('hillN20_smag0.14_full_dt0.0001_Time_2000000.txt', '1m', 0.0001,121),
     ('hillN20_smag0.14_SEM_Time_1000000.txt', '1m', 0.001,121),
    #  ('hillN40_smag0.14_SEM_Time_500000.txt', '1m', 0.001,241),
      ('hillN20_smag0.14_full_dt0.001_Time_1000000.txt', '1m', 0.001,121),
 #   ('hillN20_smag0.14_full_dt0.0001_Time_500000.txt', '1m', 0.0001,121),
   #  ('hillN20_smag0.14_full_dt0.0001_Time_1000000.txt', '1m', 0.0001,121),
    #  ('hillN20_smag0.14_full_dt0.0001_Time_1500000.txt', '1m', 0.0001,121),
    # ('hillN20_smag0.14_full_dt0.0001_Time_2000000.txt', '1m', 0.0001,121),

]
x1 = Edata[:, 0]+1
y1 = Edata[:, 1] 
x2 = Edata2[:, 0]+1
y2 = Edata2[:, 1] 

plt.rc('font', size=16)   
# Create a figure for the plot
plt.figure(figsize=(18, 5))
# Plot exp data
plt.scatter(x1, y1, marker='o', color='red', s=50, label='exp_u')

#plt.scatter(x1, y1, marker='o', color='black', s=20, label='exp_u')
#plt.plot(x2, y2, color='salmon', linewidth=2, label='OF')#colors = ['blue', 'green', 'purple', 'skyblue','steelblue']#line_styles = ['-', '--', ':', '-.', '-']
# Process and plot each dataset
# Process and plot each dataset
for i, (dataset_file, label, dt, N) in enumerate(dataset_files):
    data = np.loadtxt(dataset_file, skiprows=1)
    y = np.arange(0, 6.0, 6 / (N - 1))
    D = 2.5
    S = 1.25
    label_flag = [False, False]  # Flags to keep track of label plotting
    # Plot for each j value
    for j in range(9):
        ux_ave = data[0:(N - 1), int((j * 1.25 + 4.5) * ((N - 1) / 6) -1)] / ((N - 1) / 6*dt)
        zero_mask = ux_ave != 0  # Mask where ux_ave is not zero
        if zero_mask.any():  # Check if there are non-zero values
            if i == 0:  # For the first dataset, use a solid line
                #plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask], label=f'Ux_ave_{j} ({label})', linewidth=2)
                plt.plot(ux_ave[zero_mask] + S * (j - 0) - D, y[zero_mask], label=f'Ux_ave_{j} ({label})', linewidth=2, color='steelblue')
            elif i == 1:  # For the second dataset, use a dashed line
                plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='--', linewidth=2,color='steelblue')
            elif i == 2:  # For the second dataset, use a dashed line
                plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='-', linewidth=2,color='purple')
            elif i == 3:  # For the second dataset, use a dashed line
                plt.plot(ux_ave[zero_mask] + S * (j - 0)-D , y[zero_mask],  linestyle='--', linewidth=2,color='purple')

            zero_mask_inv = ~zero_mask
            plt.plot(np.full_like(y[zero_mask_inv], S * (j - 0)-D ), y[zero_mask_inv], color='black', linestyle='-', linewidth=8)

plt.xticks(np.arange(-5, 9, 1.25))
plt.xlim(-4, 8.75)
plt.ylim(0, 4)
plt.xlabel('X/D+u/$U_{\infty}$')
plt.ylabel('Y')
# Get only the handles and labels for solid and dashed lines

# Add legend
#plt.legend()
#plt.legend(['exp','1m',  'hill','1.5m'])
# Save the figure
#plt.savefig('N30_LBM vs CP tau.png')
plt.show()
plt.close()
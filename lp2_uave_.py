import numpy as np
import matplotlib.pyplot as plt
import math
# Define the dataset files
dataset_files = [
    #('Ud30D_output_Time_2000000.txt', 'uD_re22000', 0.000276923,181),
    ('Ucat2m_Time_1000000.txt', 'uD', 0.000276923,181),
    ('Ucat2m_Time_1500000.txt', 'uD', 0.000276923,181),
    ('Ucat2m_Time_2000000.txt', 'uD', 0.000276923,181),
   # ('Ucat30D_output_2Time_1000000.txt', '30D2', 0.000276923,181),
   # ('Ucat20D_output_Time_500000.txt', '20D', 0.000276923,181),
   # ('Ucat20D_output_2Time_500000.txt', '20D2', 0.000276923,181),
]
plt.rc('font', size=16)   
# Create a figure for the plot
plt.figure(figsize=(10, 6))

#plt.plot(x2, y2, color='salmon', linewidth=2, label='OF')#colors = ['blue', 'green', 'purple', 'skyblue','steelblue']#line_styles = ['-', '--', ':', '-.', '-']
# Process and plot each dataset
for i, (dataset_file, label, nu, N) in enumerate(dataset_files):
    data = np.loadtxt(dataset_file, skiprows=1)
    y = np.arange(0, 6.0, 6 / (N - 1))
    # Plot for each j value
    for j in range(9):
        ux_ave = data[0:(N-1), j * 30+ 75] / 0.003
        zero_mask = ux_ave != 0  # Mask where ux_ave is not zero
        if zero_mask.any():  # Check if there are non-zero values
            if i == 0:  # For the first dataset, use a solid line
                plt.plot(ux_ave[zero_mask] + 1 * j-2.5, y[zero_mask], label=f'Ux_ave_{j} ({label})')
            elif i == 1:  # For the second dataset, use a dashed line
                plt.plot(ux_ave[zero_mask] + 1 * j-2.5, y[zero_mask], '--', label=f'Ux_ave_{j} ({label})')
            elif i == 2:  # For the second dataset, use a dashed line
                plt.plot(ux_ave[zero_mask] + 1 * j-2.5, y[zero_mask], ':', label=f'Ux_ave_{j} ({label})')


plt.xlim(-2.5, 10)
plt.ylim(0, 3)
plt.xlabel('X/D+u/$U_{\infty}$')
plt.ylabel('Y')
#plt.legend()

# Save the figure
#plt.savefig('N30_LBM vs CP tau.png')
plt.show()
plt.close()
import numpy as np
import matplotlib.pyplot as plt
import math

# Read data from the file
data = np.loadtxt('output_Time_2000000.txt', skiprows=1)
DNSdata= np.loadtxt('DNS.txt', skiprows=1)

x1=DNSdata[:, 0]  
y1=DNSdata[:, 1]  
# Add parameters
nu = 0.0002769
# Extract data
x = np.arange(0.5, 31, 1) #grids in Y, N=31
#print(x)

half_length = 32
u_x = data[:half_length, 0]  
u_x_ave = data[1:half_length, 1]  # The column contains Ux_ave data and skip 0
uu = data[:, 2] 

# Calculate u+ y+ u_tau
u_tau = math.sqrt(u_x_ave[0] / (0.5) * nu)
u_plus = u_x_ave / u_tau
y_plus = u_tau * x / nu

print(u_x_ave[0])

# Plot the data
plt.figure(figsize=(8, 6))

plt.scatter(x1, y1, marker='o', color='red', s=25,  label='DNS')
plt.plot(y_plus, u_plus, label='U+', linestyle='--', marker='o')

# Use a logarithmic x-axis
plt.xscale('log')
plt.xlim(1, 130)

plt.xlabel('y+')
plt.ylabel('U+')
plt.legend()
#plt.title('Ux, Ux_ave vs. X')
plt.show()

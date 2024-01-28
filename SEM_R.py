import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import math

# Load data for Ruu, Rvv, and Rww
Edata_Ruu = np.loadtxt('Ruu.txt', delimiter=',')
Edata_Rvv = np.loadtxt('Rvv.txt', delimiter=',')
Edata_Rww = np.loadtxt('Rww.txt', delimiter=',')

# Parameters
cy = 6.0
cz = 6.0
numPoints = 40.0
resolution = 1.0 / float(numPoints)

# Generating values for y from 0 to 3.0 with a step of 0.02
y2 = np.arange(0, cy+resolution, resolution)
# Initialize arrays to store  values for Ruu, Rvv, and Rww
Ruu = np.zeros_like(y2)
Rvv = np.zeros_like(y2)
Rww = np.zeros_like(y2)
# Loop for each variable (Ruu, Rvv, Rww)
for data, _variable in zip([Edata_Ruu, Edata_Rvv, Edata_Rww], [Ruu, Rvv, Rww]):
    # Extracting data
    u_data = data[:, 0] ** 2
    y_data = data[:, 1]
    # Create an interpolation function
    interpolating_function = interp1d(y_data, u_data, kind='linear', fill_value='extrapolate')
    # Interpolating values for the new y values
    _variable[:] = interpolating_function(y2)
outputFile = "inlet_SEM.txt"
#outputFile = "outvel_y=top.txt"
# print('Interpolated values for Ruu:', _Ruu)
# print('Interpolated values for Rvv:', _Rvv)
# print('Interpolated values for Rww:', _Rww)
a = 0.10694296278590895
b = 0.753041501869327
# # Define the UX function
# def calculate_ux(cy, numPoints):
#     ux = [a * math.log(y) + b for y in range(1, int(cy * numPoints) + 1)]
#     return ux
# # Example usage
# U = calculate_ux(cy,numPoints)

f = open(outputFile, "w")

f.write("SEM\n")
f.write("U V W uu uv uw vv vw ww epsilon\n")

          
for j in range(1, int(cy * numPoints)+1):
    for k in range(0, int(cz * numPoints)):
        if j <2 :
            ux = 0
        else:
            #x_value = (j - 0) / 0.0004 / numPoints
            ux = a * math.log( (j+0)/ numPoints) + b
        k=(ux*0.03)**2*1.5
        ep=(0.09**0.75)*(k**(1.5))
        f.write(str(ux) + " " + str(0) + " " + str(0) + " " + str(Ruu[j])+ " " + str(0)+ " " + str(0)+ " " + str(Rvv[j])+ " " + str(0)+ " " + str(Rww[j])  + " " + str(ep) +"\n")

f.close()

# Plotting the original data and the interpolated curve
# plt.scatter(y, u, marker='o', color='blue', label='Original Data')
# plt.plot(y2, , color='red', label='Interpolated Curve')

# plt.xlabel('y')
# plt.ylabel('u')
# plt.legend()
# plt.show()
# plt.close()

# # Displaying the generated values for y and u
# print("Generated y values:", y2)
# print("Interpolated u values:", )
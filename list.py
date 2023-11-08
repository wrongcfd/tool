import h5py
import numpy as np
# hdf5 file to be analyzed
hdfname = 'hdf_R0N0.h5'
Gf = h5py.File(hdfname, 'r')

# Get the X, Y, and Z positions
xPos = Gf['Time_0/XPos']
yPos = Gf['Time_0/YPos']
zPos = Gf['Time_0/ZPos']
Ux = Gf['Time_400000/Ux']

x = xPos[0, 0, :]
y = yPos[0, :, 0]
z = zPos[:, 0, 0]
# Determine the valid ranges for X, Y, and Z
min_x = xPos[0]
max_x = xPos[-1]
min_y = yPos[0]
max_y = yPos[-1]
min_z = zPos[0]
max_z = zPos[-1]

mi_x = x[0]
ma_x = x[-1]
mi_y = y[0]
ma_y = y[-1]
mi_z = z[0]
ma_z = z[-1]


# 获取Ux数据集中的数据数量
ux_data_count = Ux.size

# 计算Ux数据的最小值和最大值
min_ux = np.min(Ux)
max_ux = np.max(Ux)

# 打印Ux数据数量、最小值和最大值
print(f"Ux数据数量: {ux_data_count}")
print(f"Ux数据的最小值: {min_ux}")
print(f"Ux数据的最大值: {max_ux}")
#print(f"Xpo range: {min_x} to {max_x}")
#print(f"Ypo range: {min_y} to {max_y}")
#print(f"Zpo range: {min_z} to {max_z}")

print(f"X range: {mi_x} to {ma_x}")
print(f"Y range: {mi_y} to {ma_y}")
print(f"Z range: {mi_z} to {ma_z}")
Gf.close()
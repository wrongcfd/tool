import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def convert_dos_to_unix(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        content = infile.read()

    content_unix = content.replace('\r\n', '\n')

    with open(output_file, 'w', newline='\n') as outfile:
        outfile.write(content_unix)

def generate_3d_sine_hill(amplitude_xy,  length_xy, height_xy, height_3d, resolution):
    nx = int(resolution * length_xy)
    ny = int(resolution * height_xy)
    nz = int(resolution * height_3d)

    with open(f"hill_2d.pc", "w") as ocout:
        for x in np.linspace(0, length_xy, nx):
            for y in np.linspace(0, height_xy, ny):
                for z in np.linspace(0, height_3d, nz):  # Extend to 3D by varying z
                    # Calculate the 3D sine hill function
                    radius = np.sqrt((x-2.5)**2 + (z-2.5)**2)
                    #sine_hill_xy = amplitude_xy * np.cos(2 * np.pi * frequency_xy * (np.sqrt((x-2.5)**2 + (z-2.5)**2) / length_xy))**2
                    sine_hill_xy = amplitude_xy * np.cos(np.pi * radius / length_xy)**2
                    # Check if the point is within the sine hill in XY plane
                    if radius < 2.5:
                        if y <= sine_hill_xy and not (np.isclose(x, 2.5) and np.isclose(y, 1)):
                            ocout.write(f"{x}\t{y}\t{z}\n")
                    else:
                            ocout.write(f"{x}\t{0}\t{z}\n")  # Set Z = 0 for points outside the condition

# Example usage
amplitude_value_xy = 1.0  # Change this to the desired amplitude of the sine hill in XY plane
length_value_xy = 5.0  # Change this to the desired length of the sine hill in XY plane
height_value_xy = 1.0  # Change this to the desired height of the sine hill in XY plane
height_value_3d = 5.0  # Z length
res = 21 # N+1

generate_3d_sine_hill(amplitude_value_xy, length_value_xy, height_value_xy, height_value_3d, res)

convert_dos_to_unix("hill_2d.pc", "hill_2d_unix.pc")


# Delete the "hill_2d.pc" file
file_to_delete = "hill_2d.pc"

try:
    os.remove(file_to_delete)
    print(f"{file_to_delete} deleted successfully")
except OSError as e:
    print(f"Deletion failed: {e}")

# # Load data from the file
file_path = "hill_2d_unix.pc"  # Change this to the correct file path
data = np.loadtxt(file_path)

# # Extract coordinates
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Plot the 3D sine hill
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=1, c='blue', marker='o')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Sine Hill')

plt.show()
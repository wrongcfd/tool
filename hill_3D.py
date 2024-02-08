import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

def convert_dos_to_unix(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        content = infile.read()

    content_unix = content.replace('\r\n', '\n')

    with open(output_file, 'w', newline='\n') as outfile:
        outfile.write(content_unix)

def generate_3d_sine_hill(amplitude_xy, frequency_xy, length_xy, height_xy, height_3d, resolution):
    nx = int(resolution * length_xy)
    ny = int(resolution * height_xy)
    nz = int(resolution * height_3d)

    points = []

    for x in np.linspace(0, length_xy, nx):
        for y in np.linspace(0, height_xy, ny):
            for z in np.linspace(0, height_3d, nz):  # Extend to 3D by varying z
                # Calculate the 2D sine hill function
                sine_hill_xy = amplitude_xy * np.cos(2 * np.pi * frequency_xy * ((x-2.5)/ length_xy))**2
                # Check if the point is within the sine hill in XY plane and not at the specified coordinates
                if y <= sine_hill_xy and not (np.isclose(x, 2.5) and np.isclose(y, 1)):
                    points.append([x, y, z])

    # Find the maximum X value for each Y and set it as radius
    max_x_for_y = {}
    for point in points:
        y_value = point[1]
        x_value = point[0]
        if y_value not in max_x_for_y or x_value > max_x_for_y[y_value]:
            max_x_for_y[y_value] = x_value

    # Create a new list for the final points
    final_points = []
    for point in points:
        x, y, z = point
        radius = abs(max_x_for_y[y] - 2.5)
        print(f"radius: {radius:.2f}")
        if (x - 2.5)**2 + (z - 2.5)**2 <= radius**2:
            final_points.append([x, y, z])

    return np.array(final_points)

# Example usage
amplitude_value_xy = 1.0
frequency_value_xy = 0.5
length_value_xy = 5.0
height_value_xy = 1.0
height_value_3d = 5.0
res = 21

# Generate points using the sine hill function
points_sine_hill_3d = generate_3d_sine_hill(amplitude_value_xy, frequency_value_xy, length_value_xy, height_value_xy, height_value_3d, res)

# Save points to file
np.savetxt("sine_hill_function_3d.pc", points_sine_hill_3d, delimiter='\t', fmt='%.3f', comments='')

# Convert the generated and existing files to UNIX line endings
convert_dos_to_unix("sine_hill_function_3d.pc", "sine_hill_function_3d_unix.pc")
# 指定要删除的文件路径

file_to_delete = "sine_hill_function_3d.pc"

# 尝试删除文件
try:
    os.remove(file_to_delete)
    print(f"{file_to_delete} 删除成功")
except OSError as e:
    print(f"删除失败: {e}")


# Plot the 3D sine hill points
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(points_sine_hill_3d[:, 0], points_sine_hill_3d[:, 1], points_sine_hill_3d[:, 2], s=50, c='red', marker='o', label='sine_hill_function_3d.pc')

# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('3D Sine Hill Function')

# plt.legend()
# plt.show()

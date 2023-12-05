import numpy as np

def generate_disk(radius, resolution):
    ny = resolution
    nz = resolution
    cy = radius_value
    cz = radius_value

    #with open(f"disk_{resolution}.pc", "w") as ocout:
    with open(f"disk_31.pc", "w") as ocout:
        for y in np.linspace(0, 1, ny):
            for z in np.linspace(0, 1, nz):
                # Check if the point is within the disk
                if (y-cy)**2 + (z-cz)**2 <= radius**2:  # Adjusted center to (0.5, 0.5)
                    ocout.write(f"0.0\t{y}\t{z}\n")

# Example usage
radius_value = 0.5  # Change this to the desired radius
generate_disk(radius_value, resolution=31)

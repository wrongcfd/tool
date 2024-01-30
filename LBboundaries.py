# Writes the coordinates inside the defined cube in a text file in the format 
# (x y z)
# (x y z)
# ...

# User input: cell size
d = 1.0/5

# User input: List of the minimum x value (xmin), y value (ymin), and z value (zmin) for each of the GASCANS boundaries. 
xmin = 0 + d / 2.0
ymin = 0 + 3 * d / 2.0
zmin = d / 2.0

# User input: List of the maximum x value (xmax), y value (ymax), and z value (zmax) for each of the GASCANS boundaries. 
xmax = 0 + d / 2.0
ymax = 6.0 + d / 2.0
zmax = 6.0 - d / 2.0

# User input: Name of the GASCANS boundaries. The names are used in the file name for each boundary.
wall_name = 'LB_left'

Nx = int((xmax - xmin) / d + 1.5)
Ny = int((ymax - ymin) / d + 1.5)
Nz = int((zmax - zmin) / d + 1.5)

fcoordname = "GASCANS" + wall_name + ".txt"
fcoord = open(fcoordname, "w")

for i in range(0, Nx):
    for j in range(0, Ny):
        for k in range(0, Nz):
            fcoord.write(str(xmin + i * d) + " " + str(ymin + j * d) + " " + str(zmin + k * d) + "\n")

fcoord.close()

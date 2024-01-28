# Writes the coordinates inside the defined cube in a text file in the format 
# (x y z)
# (x y z)
# ...

# User input: cell size
d = 1.0/40

# User input: List of the minium x value (xmin), y value (ymin) and z value (zmin) for each of the GASCANS boundaries. In this example there are 4 boundaries. 
xmin = 0+ d / 2.0,3
ymin = 0+ 3*d / 2.0,3
zmin = d / 2.0,3

# User input: List of the maximum x value (xmax), y value (ymax) and z value (zmax) for each of the GASCANS boundaries. In this example there are 4 boundaries. 
xmax = 0 + d / 2.0,3
ymax = 6.0 + d/2.0,3
zmax = 6.0 - d / 2.0,3

# User input: Name of the GASCANS boundaries. The names are used in the file name for each boundary. 
wall_name = 'LB_left','right'

for p in range(0,len(xmin)):

	Nx = int((xmax[p] - xmin[p]) / d + 1.5) 
	Ny = int((ymax[p] - ymin[p]) / d + 1.5)
	Nz = int((zmax[p] - zmin[p]) / d + 1.5)


	fname = "sampleDictCoord" + wall_name[p]
	fcoordname = "GASCANS" + wall_name[p] + ".txt"
	f = open(fname, "w")
	fcoord = open(fcoordname, "w")

	for i in range(0,Nx):
		for j in range(0,Ny):
			for k in range(0,Nz):

				f.write("( " + str(xmin[p] + i*d) + " " + str(ymin[p] + j*d) + " " + str(zmin[p] + k*d) + " )\n")
				fcoord.write(str(xmin[p] + i*d) + " " + str(ymin[p] + j*d) + " " + str(zmin[p] + k*d) + "\n")

	f.close()
	fcoord.close()

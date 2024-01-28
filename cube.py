import numpy as np

dx= 1/20
Lx = 1.0  # cube size in physical
Ly = Lx
nx = int(Lx/dx) + 1   # total grids 
ny = nx
nz = nx

a = np.zeros((nx, ny, nz))

with open("cube_40.pc", "w") as ocout:
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                a[x][y][z] = x * dx
                ocout.write(f"{a[x][y][z]}\t")
                a[x][y][z] = y * dx
                ocout.write(f"{a[x][y][z]}\t")
                a[x][y][z] = z * dx
                ocout.write(f"{a[x][y][z]}\n")